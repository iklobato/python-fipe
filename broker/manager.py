from celery import Celery


class CeleryConnector:
    def __init__(self, broker_url, backend_url):
        self.broker_url = broker_url
        self.backend_url = backend_url
        self._app = self.connect()

    def connect(self):
        self._app = Celery('tasks', broker=self.broker_url, backend=self.backend_url)
        return self._app

    @property
    def app(self):
        print("app: ", self._app)
        return self._app


class CeleryProducer:
    def __init__(self, app):
        self.app = app

    def send_task(self, task_name, *args, **kwargs):
        task = self.app.send_task(task_name, args=args, kwargs=kwargs)
        return task


class CeleryConsumer:
    def __init__(self, app, queue_name):
        self.app = app
        self.queue_name = queue_name

    def start_consuming(self):
        with self.app.connection() as connection:
            worker = self.app.Worker(connection=connection, queues=[self.queue_name])
            worker.start()


if __name__ == '__main__':
    celer = CeleryConnector(broker_url="redis://localhost:6379/0", backend_url="redis://localhost:6379/0")
    celer.connect()

    # producer = CeleryProducer(celer.app)
    # producer.send_task("tasks.add", 1, 2)
    #
    consumer = CeleryConsumer(celer.app, "tasks")
    consumer.start_consuming()
