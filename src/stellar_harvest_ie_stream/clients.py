import json

from stellar_harvest_ie_config.utils.log_decorators import log_io
from kafka import KafkaProducer, KafkaConsumer
from stellar_harvest_ie_stream.settings import settings


_producer: KafkaProducer | None = None


@log_io()
def get_producer() -> KafkaProducer:
    global _producer
    if _producer is None:
        _producer = KafkaProducer(
            bootstrap_servers=[settings.kafka_uri],
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
            acks="all",
            retries=5,
            retry_backoff_ms=300,
            linger_ms=10,
            # compression_type="gzip",
        )
    return _producer


@log_io()
def get_consumer(topic: str, group_id: str):
    return KafkaConsumer(
        topic,
        bootstrap_servers=[settings.kafka_uri],
        group_id=group_id,
        value_deserializer=lambda b: json.loads(b.decode()),
        auto_offset_reset="earliest",
    )
