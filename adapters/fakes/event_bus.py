class FakeEventBus:
    def __init__(self):
        self.events = []

    def publish(self, event: dict) -> None:
        self.events.append(event)

    def get_events(self) -> list[dict]:
        return self.events.copy()
