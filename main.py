from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fuzzywuzzy.fuzz import ratio

from broker.tasks import load_data, DataLoader
from config import (
    FIPE_BASE_URL,
)
from apis.base import SessionManager
from apis.fipe import FipeApi

app = FastAPI()  # api 1

sm = SessionManager()
fipe_base_api = FipeApi(base_url=FIPE_BASE_URL, session_manager=sm)
data_loader = DataLoader(fipe_base_api)


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")


@app.get("/api/load")
async def fipe_marcas(limit: int = 10):
    """
    Load limit:int data from FIPE API to the database
    :param limit: limit of data to be loaded
    :return: status of the operation
    """
    load_data(limit=limit)
    return {"status": "ok"}


@app.get("/api/marcas")
async def fipe_marcas(marca_nome: str = None):
    """
    Get all brands or filter by name
    :param marca_nome: name of the brand
    :return: list of car models belonging to the brand
    """
    if not marca_nome:
        return data_loader.load_marcas()
    result = data_loader.load_marcas()
    result = [marca for marca in result if ratio(marca.get('nome'), marca_nome) > 80]
    marca_id = result[0].get('codigo')
    return data_loader.load_modelos(carro_id=marca_id)


@app.patch("/api/marcas")
async def fipe_marcas():
    response = data_loader.load_marcas()
    return response
