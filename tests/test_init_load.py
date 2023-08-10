import os
import json
from unittest import TestCase
from unittest.mock import patch

from apis.fipe import FipeApi
from broker.tasks import DataLoader
from config import FIPE_BASE_URL
from models.fipe import Marca, Modelo, Ano, Valor


class TestInitialLoad(TestCase):

    def setUp(self) -> None:
        self.data_loader = DataLoader(FipeApi(base_url=FIPE_BASE_URL))

        self.marcas_response = open(
            os.path.dirname(os.path.abspath(__file__)) + '/mocks/marcas.json'
        ).read()

        self.modelos_response = open(
            os.path.dirname(os.path.abspath(__file__)) + '/mocks/modelos.json'
        ).read()

        self.anos_response = open(
            os.path.dirname(os.path.abspath(__file__)) + '/mocks/anos.json'
        ).read()

        self.valores_response = open(
            os.path.dirname(os.path.abspath(__file__)) + '/mocks/valores.json'
        ).read()

    def test_load_marcas_object(self):
        with patch('broker.tasks.request_url') as mock_request:
            mock_request.return_value = json.loads(self.marcas_response)
            result = self.data_loader.load_marcas()
            for m in result:
                m = Marca(**m)
                self.assertIsInstance(m, Marca)
                self.assertIsInstance(m.codigo, str)
                self.assertIsInstance(m.nome, str)

    def test_load_modelos_object(self):
        with patch('broker.tasks.request_url') as mock_request:
            mock_request.return_value = json.loads(self.modelos_response).get('modelos')
            result = self.data_loader.load_modelos(carro_id=1)
            for model in result:
                m = Modelo(**model)
                self.assertIsInstance(m, Modelo)
                self.assertIsInstance(m.codigo, int)
                self.assertIsInstance(m.nome, str)

    def test_load_anos_object(self):
        with patch('broker.tasks.request_url') as mock_request:
            mock_request.return_value = json.loads(self.anos_response)
            result = self.data_loader.load_anos(carro_id=1, modelo_id=1)
            for ano in result:
                a = Ano(**ano)
                self.assertIsInstance(a, Ano)
                self.assertIsInstance(a.codigo, str)
                self.assertIsInstance(a.nome, str)

    def test_load_valores_object(self):
        with patch('broker.tasks.request_url') as mock_request:
            mock_request.return_value = json.loads(self.valores_response)
            result = self.data_loader.load_valores(carro_id=1, modelo_id=1, ano_id=1)
            for valor in result:
                v = Valor(**valor)
                self.assertIsInstance(v, Valor)
                self.assertIsInstance(v.tipo_veiculo, int)
                self.assertIsInstance(v.valor, str)
                self.assertIsInstance(v.marca, str)
                self.assertIsInstance(v.modelo, str)
                self.assertIsInstance(v.ano_modelo, int)
                self.assertIsInstance(v.combustivel, str)
                self.assertIsInstance(v.codigo_fipe, str)
                self.assertIsInstance(v.mes_referencia, str)
                self.assertIsInstance(v.sigla_combustivel, str)
