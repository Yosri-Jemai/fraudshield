from adapters.fakes.event_bus import FakeEventBus


def test_publish_event():
    bus = FakeEventBus()
    event = {"type": "fraud_detected", "transaction_id": "tx1"}

    bus.publish(event)

    assert bus.get_events() == [event]


def test_publish_multiple_events():
    bus = FakeEventBus()
    bus.publish({"type": "created"})
    bus.publish({"type": "updated"})

    assert len(bus.get_events()) == 2


def test_events_initially_empty():
    bus = FakeEventBus()

    assert bus.get_events() == []
