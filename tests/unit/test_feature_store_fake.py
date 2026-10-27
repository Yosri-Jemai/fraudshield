from adapters.fakes.feature_store import FakeFeatureStore


def test_save_and_get_features():
    store = FakeFeatureStore()
    values = {"amount": 150.0, "transaction_count": 5.0}

    store.save("user1", values)

    assert store.get("user1") == values


def test_get_missing_features():
    store = FakeFeatureStore()

    assert store.get("unknown") is None


def test_update_features():
    store = FakeFeatureStore()
    store.save("user1", {"amount": 100.0})
    store.save("user1", {"amount": 200.0})

    assert store.get("user1") == {"amount": 200.0}
