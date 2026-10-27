from adapters.fakes.object_store import FakeObjectStore


def test_put_and_get():
    store = FakeObjectStore()
    store.put("report.csv", "amount,country\n100,Tunisia")

    assert store.get("report.csv") == "amount,country\n100,Tunisia"


def test_get_missing_object():
    store = FakeObjectStore()

    assert store.get("missing.csv") is None


def test_delete_object():
    store = FakeObjectStore()
    store.put("report.csv", "data")
    store.delete("report.csv")

    assert store.get("report.csv") is None
