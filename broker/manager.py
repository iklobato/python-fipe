import asyncio

from aiokafka import AIOKafkaProducer, AIOKafkaConsumer


class Kafka:
    instance = None

    def __init__(self, port, host) -> None:
        self.port = port
        self.host = host

    @property
    def topic(self):
        return self.topic

    @topic.setter
    def topic(self, value):
        self.topic = value


class KafkaProducer(Kafka):
    def __init__(self, port, host) -> None:
        super().__init__(port, host)
        self.producer = AIOKafkaProducer(
            bootstrap_servers=f"{self.host}:{self.port}",
            loop=asyncio.get_event_loop(),
        )

    async def connect(self):
        await self.producer.start()

    async def send(self, topic, message):
        await self.producer.send_and_wait(topic, message.encode("utf-8"))

    async def disconnect(self):
        await self.producer.stop()


class KafkaConsumer(Kafka):
    def __init__(self, port, host) -> None:
        super().__init__(port, host)
        self.consumer = AIOKafkaConsumer(
            self.topic,
            bootstrap_servers=f"{self.host}:{self.port}",
            loop=asyncio.get_event_loop(),
        )

    async def connect(self):
        await self.consumer.start()

    async def consume(self):
        async for msg in self.consumer:
            print("consumed: ", msg.topic, msg.partition, msg.offset,
                  msg.key, msg.value, msg.timestamp)

    async def disconnect(self):
        await self.consumer.stop()
