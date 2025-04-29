import json
import datetime
import pytest
from stellar_harvest_ie_stream.clients import get_producer, get_consumer
from stellar_harvest_ie_stream.settings import settings


def test_get_producer_calls_KafkaProducer_with_correct_args(mocker):
    fake_producer = object()
    mock_kp = mocker.patch(
        "stellar_harvest_ie_stream.clients.KafkaProducer", return_value=fake_producer
    )
    producer = get_producer()

    mock_kp.assert_called_once()
    args, kwargs = mock_kp.call_args
    assert kwargs["bootstrap_servers"] == [settings.kafka_uri]

    serializer = kwargs["value_serializer"]
    # test serialization of datetime via default=str
    dt = datetime.datetime(1970, 1, 1, 12, 0, 0)
    serialized = serializer({"timestamp": dt})
    expected = json.dumps({"timestamp": dt}, default=str).encode()
    assert serialized == expected
    assert producer is fake_producer


def test_get_consumer_calls_KafkaConsumer_with_correct_args(mocker):
    topic = "some-topic"
    group = "some-group"

    fake_consumer = object()
    mock_kc = mocker.patch(
        "stellar_harvest_ie_stream.clients.KafkaConsumer", return_value=fake_consumer
    )
    consumer = get_consumer(topic, group)
    
    mock_kc.assert_called_once()
    args, kwargs = mock_kc.call_args
    assert args == (topic,)
    assert kwargs["bootstrap_servers"] == [settings.kafka_uri]
    assert kwargs["group_id"] == group

    deserializer = kwargs["value_deserializer"]
    # test deserialization
    message = {"key": "value"}
    raw = json.dumps(message).encode()
    assert deserializer(raw) == message
    assert kwargs["auto_offset_reset"] == "earliest"
    assert consumer is fake_consumer
