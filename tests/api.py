from unittest import TestCase

from apis.fipe import FipeApi
from config import (
    FIPE_BASE_URL,
    FIPE_API_MARCAS,
    FIPE_API_ANOS,
    FIPE_API_MODELOS,
    FIPE_API_VALOR,
)


class TestUrlBuilder(TestCase):

    def setUp(self) -> None:
        self.fipe_api = FipeApi(base_url=FIPE_BASE_URL)
        self.base_url = FIPE_BASE_URL

    def test_build_url_marcas(self):
        url = self.fipe_api.build_url(subpath=FIPE_API_MARCAS)
        self.assertEqual(url, f'{self.base_url}/carros/marcas')

    def test_build_url_modelos(self):
        url = self.fipe_api.build_url(subpath=FIPE_API_MODELOS, carro_id=1)
        self.assertEqual(url, f'{self.base_url}/carros/marcas/1/modelos')

    def test_build_url_anos(self):
        url = self.fipe_api.build_url(subpath=FIPE_API_ANOS, carro_id=1, modelo_id=1)
        self.assertEqual(url, f'{self.base_url}/carros/marcas/1/modelos/1/anos')

    def test_build_url_valores(self):
        url = self.fipe_api.build_url(subpath=FIPE_API_VALOR, carro_id=1, modelo_id=1, ano_id=1)
        self.assertEqual(url, f'{self.base_url}/carros/marcas/1/modelos/1/anos/1')
