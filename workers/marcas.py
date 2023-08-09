from apis.base import BaseApi
from workers.base import BaseWorker


class FipeMarcasWorker(BaseWorker, BaseApi):

    def __init__(self, api: BaseApi, sub_path: str, celery_instance: object) -> None:
        super().__init__(api=api, celery_instance=celery_instance)
        self.sub_path = sub_path

    async def run(self):
        url = self.get_url()
        response = await self.session.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Não foi possível obter as marcas"}

    async def get_url(self):
        return f"{self.base_url}{self.sub_path}"
