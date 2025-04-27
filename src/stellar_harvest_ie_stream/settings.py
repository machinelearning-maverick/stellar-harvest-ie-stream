import logging

from pydantic import Field
from pydantic_settings import BaseSettings

logger = logging.getLogger(__name__)


class StreamSettings(BaseSettings):
    logger.info("StreamSettings()")
    kafka_uri: str = Field("localhost:9092", env="KAFKA_URI")
    swpc_topic: str = Field("raw-space-weather", env="KAFKA_TOPIC_SWPC")

    class Config:
        env_file = ""
        env_file_encoding = "utf-8"


settings = StreamSettings()
