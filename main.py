import os

from fastapi import FastAPI

from broker.manager import Kafka
from config import (
    FIPE_BASE_URL,
    FIPE_API_MARCAS,
    FIPE_API_ANOS,
    FIPE_API_MODELOS,
    FIPE_API_VALOR,
    KAFKA_HOST,
    KAFKA_PORT,
)
from apis.base import SessionManager
from apis.fipe import FipeApi
from workers.anos import FipeAnosWorker
from workers.marcas import FipeMarcasWorker
from workers.modelos import FipeModelosWorker
from workers.valor import FipeValorWorker

app = FastAPI()

fipe_base_api = FipeApi(base_url=FIPE_BASE_URL, session_manager=SessionManager())

kafka_server = Kafka(
    port=KAFKA_PORT,
    host=KAFKA_HOST
)
fipe_marcas_worker = FipeMarcasWorker(api=fipe_base_api, sub_path=FIPE_API_MARCAS)
fipe_anos_worker = FipeAnosWorker(api=fipe_base_api, sub_path=FIPE_API_ANOS)
fipe_modelos_worker = FipeModelosWorker(api=fipe_base_api, sub_path=FIPE_API_MODELOS)
fipe_valor_worker = FipeValorWorker(api=fipe_base_api, sub_path=FIPE_API_VALOR)


@app.get("/")
async def root():
    return {"status": "ok"}


@app.get("/api/fipe/marcas")
async def fipe_marcas():
    return await fipe_marcas_worker.run()
