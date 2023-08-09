from random import shuffle

from apis.base import SessionManager
from broker.celery_app import celery_app
from config import (
    FIPE_BASE_URL,
    FIPE_API_MARCAS,
    FIPE_API_ANOS,
    FIPE_API_MODELOS,
    FIPE_API_VALOR,
)


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


@celery_app.task(acks_late=True)
def save_on_db(data: dict):
    """
    Saves data to the database
    :param data: data to be saved
    :return: status of the operation
    """
    pass


def load_data(limit: int = 100):
    """
    Load limit:int data from FIPE API to the database
    :param limit: limit of data to be loaded
    :return: status of the operation
    """
    def load_marcas():
        url = f"{FIPE_BASE_URL}{FIPE_API_MARCAS}"
        result = request_url.delay(url)
        return [{"marca": marca["nome"], "marca_id": marca["codigo"]} for marca in result.get()]

    def load_modelos(carro_id: int):
        url = f"{FIPE_BASE_URL}{FIPE_API_MODELOS}"
        url = url.format(carro_id=carro_id)
        result = request_url.delay(url)
        return [{"modelo": modelo["nome"], "modelo_id": modelo["codigo"]} for modelo in result.get()]

    def load_anos(carro_id: int, modelo_id: int):
        url = f"{FIPE_BASE_URL}{FIPE_API_ANOS}"
        url = url.format(carro_id=carro_id, modelo_id=modelo_id)
        result = request_url.delay(url)
        return [{"ano": ano["nome"], "ano_id": ano["codigo"]} for ano in result.get()]

    def load_valores(carro_id: int, modelo_id: int, ano_id: int):
        url = f"{FIPE_BASE_URL}{FIPE_API_VALOR}"
        url = url.format(carro_id=carro_id, modelo_id=modelo_id, ano_id=ano_id)
        result = request_url.delay(url)
        return [{"valor": valor["Valor"], "mes_referencia": valor["MesReferencia"], "combustivel": valor["Combustivel"]} for valor in result.get()]

    sample = load_marcas()
    shuffle(sample)
    total = 0
    for marca in sample:
        marca_id = marca["marca_id"]
        modelos = load_modelos(marca_id)
        for modelo in modelos:
            modelo_id = modelo["modelo_id"]
            anos = load_anos(marca_id, modelo_id)
            for ano in anos:
                ano_id = ano["ano_id"]
                valores = load_valores(marca_id, modelo_id, ano_id)
                for valor in valores:
                    total += 1
                    if total >= limit:
                        return {"status": "ok"}
