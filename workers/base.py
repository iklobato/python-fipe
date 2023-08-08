from abc import ABC

from apis.base import BaseApi


class BaseWorker(ABC):
    """
    Base class for all async workers in the project
    """

    def __init__(self, api: BaseApi, kafka_instance: object):
        self.api = api
        self.kafka = kafka_instance

    async def run(self):
        raise NotImplementedError
