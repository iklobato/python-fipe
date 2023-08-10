from functools import lru_cache
from pprint import pprint
from random import shuffle
from typing import List, Dict

from apis.base import SessionManager
from apis.fipe import FipeApi
from broker.celery_app import celery_app
from config import (
    FIPE_BASE_URL,
    FIPE_API_MARCAS,
    FIPE_API_ANOS,
    FIPE_API_MODELOS,
    FIPE_API_VALOR,
)
from models.fipe import Marca, Modelo, Ano


@celery_app.task(acks_late=True)
def request_url(url: str, params: dict = None, method: str = 'get') -> dict:
    """
    Makes a request to a given url and returns the response as a dict
    :param url: url to be requested
    :param params: params to be passed to the request
    :param method: request method, defaults to 'get'
    :return: response as a dict
    """
    print(f"Requesting {url}")
    session = SessionManager()
    response = session.request(method=method, url=url, params=params)
    return response.json()


class DataLoader:
    """
    Loads data from FIPE API to the database using Celery tasks.
    """

    __cache_max_size = 128

    def __init__(self, api: FipeApi):
        self.api = api

    def camel_to_snake(self, s: str) -> str:
        return ''.join(['_' + c.lower() if c.isupper() else c for c in s]).lstrip('_')

    @lru_cache(maxsize=__cache_max_size)
    def load_marcas(self) -> List[Dict]:
        url = self.api.build_url(subpath=FIPE_API_MARCAS)
        result = request_url.delay(url)
        result = result.get(timeout=10)
        return [{**marca} for marca in result]

    @lru_cache(maxsize=__cache_max_size)
    def load_modelos(self, carro_id: str) -> List[Dict]:
        url = self.api.build_url(subpath=FIPE_API_MODELOS, carro_id=carro_id)
        result = request_url.delay(url)
        result = result.get(timeout=10)
        return [{**modelo} for modelo in result.get('modelos')]

    @lru_cache(maxsize=__cache_max_size)
    def load_anos(self, carro_id: str, modelo_id: int) -> List[Dict]:
        url = self.api.build_url(subpath=FIPE_API_ANOS, carro_id=carro_id, modelo_id=modelo_id)
        result = request_url.delay(url)
        result = result.get(timeout=10)
        return [{**ano} for ano in result]

    @lru_cache(maxsize=__cache_max_size)
    def load_valores(self, carro_id: str, modelo_id: int, ano_id: str) -> List[Dict]:
        url = self.api.build_url(subpath=FIPE_API_VALOR, carro_id=carro_id, modelo_id=modelo_id, ano_id=ano_id)
        result = request_url.delay(url)
        result = [result.get(timeout=10)]
        response = [{self.camel_to_snake(k): v for k, v in valor.items()} for valor in result]
        return response


def load_data(limit: int = 100):
    """
    Load limit:int data from FIPE API to the database
    :param limit: limit of data to be loaded
    :return: status of the operation
    """
    fipe_base_api = FipeApi(base_url=FIPE_BASE_URL)
    data_loader = DataLoader(fipe_base_api)

    sample = data_loader.load_marcas()
    shuffle(sample)
    total = 0
    for marca in sample:
        marca_obj = Marca(**marca)
        modelos = data_loader.load_modelos(marca_obj.codigo)
        shuffle(modelos)
        for modelo in modelos:
            modelo_obj = Modelo(**modelo)
            anos = data_loader.load_anos(marca_obj.codigo, modelo_obj.codigo)
            shuffle(anos)
            for ano in anos:
                ano_obj = Ano(**ano)
                valores = data_loader.load_valores(marca_obj.codigo, modelo_obj.codigo, ano_obj.codigo)
                for valor in valores:
                    total += 1
                    pprint(
                        {
                            "marca": marca_obj,
                            "modelo": modelo_obj,
                            "ano": ano_obj,
                            "valor": valor,
                        }
                    )
                    if total >= limit:
                        return True


if __name__ == '__main__':
    # request_url.delay = request_url  # monkey patching to make it work with __main__
    # request_url.get = lambda self: self.get(timeout=10)

    load_data(limit=1)
