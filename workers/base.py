from abc import ABC

from apis.base import BaseApi


class BaseWorker(ABC):
    """
    Base class for all async workers in the project
    """

    def __init__(self, api: BaseApi, celery_instance: object):
        self.api = api
        self.celery_instance = celery_instance

    async def run(self):
        raise NotImplementedError


class BaseProducer(ABC):
    """
    Base class for all async producers in the project. Can add tasks to a queue
    """

    def __init__(self, celery_instance: object):
        self.celery_instance = celery_instance

    async def enqueue(self):
        raise NotImplementedError
