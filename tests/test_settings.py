import pytest
from stellar_harvest_ie_stream.settings import StreamSettings


def test_default_stream_settings(tmp_path, monkeypatch):
    # Ensure no env-vars override defaults
    monkeypatch.delenv("KAFKA_URI", raising=False)
    monkeypatch.delenv("KAFKA_TOPIC_SWPC", raising=False)

    settings = StreamSettings(_env_file=None)
    assert settings.kafka_uri == "localhost:9092"
    assert settings.swpc_topic == "raw-space-weather"
