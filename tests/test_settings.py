import pytest
import importlib

from pytest import MonkeyPatch
from stellar_harvest_ie_stream.settings import StreamSettings, KAFKA_URI, KAFKA_TOPIC_SWPC

import stellar_harvest_ie_stream.settings as settings_module


def test_default_stream_settings(monkeypatch):
    # Ensure no env-vars override defaults
    monkeypatch.delenv(KAFKA_URI, raising=False)
    monkeypatch.delenv(KAFKA_TOPIC_SWPC, raising=False)

    # instantiate without env file
    ss = StreamSettings()
    assert ss.kafka_uri == "kafka:9092"
    assert ss.swpc_topic == "stellar-harvest-ie-raw-space-weather"


def test_env_override_streamsettings(monkeypatch):
    with monkeypatch.context() as mp:
        mp.setenv(KAFKA_URI, "example:1234")
        mp.setenv(KAFKA_TOPIC_SWPC, "custom-topic")

        importlib.reload(settings_module)

        ss = StreamSettings()
        assert ss.kafka_uri == "example:1234"
        # assert ss.swpc_topic == "custom-topic"
