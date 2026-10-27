class FakeRepository:
    def __init__(self):
        self.data = {}

    def save(self, record_id: str, record: dict) -> None:
        self.data[record_id] = record

    def get(self, record_id: str) -> dict | None:
        return self.data.get(record_id)

    def delete(self, record_id: str) -> None:
        self.data.pop(record_id, None)
