from abc import ABC

from apis.base import BaseApi


class FipeApi(BaseApi):

    sub_path = ""

    async def get(self, endpoint, **kwargs):
        async with self.session.get(url=f"{self.base_url}{endpoint}", **kwargs) as response:
            return response

    async def post(self, endpoint, **kwargs):
        async with self.session.post(url=f"{self.base_url}{endpoint}", **kwargs) as response:
            return response

    async def put(self, endpoint, **kwargs):
        async with self.session.put(url=f"{self.base_url}{endpoint}", **kwargs) as response:
            return response

    async def delete(self, endpoint, **kwargs):
        async with self.session.delete(url=f"{self.base_url}{endpoint}", **kwargs) as response:
            return response
