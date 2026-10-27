class FakeObjectStore:
    def __init__(self):
        self.objects = {}

    def put(self, key: str, content: str) -> None:
        self.objects[key] = content

    def get(self, key: str) -> str | None:
        return self.objects.get(key)

    def delete(self, key: str) -> None:
        self.objects.pop(key, None)
