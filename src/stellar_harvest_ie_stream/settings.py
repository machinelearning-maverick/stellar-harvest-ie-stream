from pydantic import Field
from pydantic_settings import BaseSettings


class StreamSettings(BaseSettings):
    kafka_uri: str = Field("localhost:9092", env="KAFKA_URI")
    swpc_topic: str = Field("raw-space-weather", env="KAFKA_TOPIC_SWPC")

    class Config:
        env_file = ""
        env_file_encoding = "utf-8"


settings = StreamSettings()
