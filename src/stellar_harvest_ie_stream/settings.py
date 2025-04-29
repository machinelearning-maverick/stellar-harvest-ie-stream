import logging

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger(__name__)

KAFKA_URI = "KAFKA_URI"
KAFKA_TOPIC_SWPC = "KAFKA_TOPIC_SWPC"


class StreamSettings(BaseSettings):
    logger.info("StreamSettings()")

    model_config = SettingsConfigDict(env_file=None)

    kafka_uri: str = Field("localhost:9092", env=KAFKA_URI)
    swpc_topic: str = Field("raw-space-weather", env=KAFKA_TOPIC_SWPC)


settings = StreamSettings()
