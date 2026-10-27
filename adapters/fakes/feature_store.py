class FakeFeatureStore:
    def __init__(self):
        self.features = {}

    def save(self, entity_id: str, values: dict[str, float]) -> None:
        self.features[entity_id] = values

    def get(self, entity_id: str) -> dict[str, float] | None:
        return self.features.get(entity_id)
