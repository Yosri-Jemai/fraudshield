class FakeModelRegistry:
    def __init__(self):
        self.models = {}

    def register(self, name: str, version: str, path: str) -> None:
        self.models[(name, version)] = {"path": path}

    def get(self, name: str, version: str) -> dict | None:
        return self.models.get((name, version))
