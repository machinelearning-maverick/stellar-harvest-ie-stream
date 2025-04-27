import json

from stellar_harvest_ie_config.utils.log_decorators import log_io
from kafka import KafkaProducer, KafkaConsumer
from .settings import settings


@log_io()
def get_producer() -> KafkaProducer:
    return KafkaProducer(
        bootstrap_servers=[settings.kafka_uri],
        value_serializer=lambda v: json.dumps(v, default=str).encode(),
    )


@log_io()
def get_consumer(topic: str, group_id: str):
    return KafkaConsumer(
        topic,
        bootstrap_servers=[settings.kafka_uri],
        group_id=group_id,
        value_deserializer=lambda b: json.loads(b.decode()),
        auto_offset_reset="earliest",
    )
