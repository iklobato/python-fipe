import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

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
async def fipe_marcas():
    response = data_loader.load_marcas()
    return response


@app.patch("/api/marcas")
async def fipe_marcas():
    response = data_loader.load_marcas()
    return response


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

