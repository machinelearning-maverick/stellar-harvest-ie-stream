import logging

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger(__name__)

KAFKA_URI = "KAFKA_URI"
KAFKA_TOPIC_SWPC = "KAFKA_TOPIC_SWPC"


class StreamSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=None)

    kafka_uri: str = Field("kafka:9092", env=KAFKA_URI)
    swpc_topic: str = Field(
        "stellar-harvest-ie-raw-space-weather", env=KAFKA_TOPIC_SWPC
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        logger.info("StreamSettings()")


settings = StreamSettings()
