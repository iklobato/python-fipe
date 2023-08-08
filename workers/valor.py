from apis.base import BaseApi
from workers.base import BaseWorker


class FipeValorWorker(BaseWorker, BaseApi):

    def __init__(self, api: BaseApi, sub_path: str = None):
        super().__init__(api=api)
        self.sub_path = sub_path

    async def run(self):
        response = await self.session.get(endpoint="/carros/marcas")

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Não foi possível obter as marcas"}

    async def enqueue(self):
        pass
