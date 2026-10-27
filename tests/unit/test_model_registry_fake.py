from adapters.fakes.model_registry import FakeModelRegistry


def test_register_and_get_model():
    registry = FakeModelRegistry()
    registry.register("fraud-detector", "v1", "models/fraud_v1.pkl")

    assert registry.get("fraud-detector", "v1") == {"path": "models/fraud_v1.pkl"}


def test_get_missing_model():
    registry = FakeModelRegistry()

    assert registry.get("unknown", "v1") is None


def test_multiple_model_versions():
    registry = FakeModelRegistry()
    registry.register("fraud-detector", "v1", "models/v1.pkl")
    registry.register("fraud-detector", "v2", "models/v2.pkl")

    assert registry.get("fraud-detector", "v1")["path"] == "models/v1.pkl"
    assert registry.get("fraud-detector", "v2")["path"] == "models/v2.pkl"
