from adapters.fakes.cache import FakeCache


def test_set_and_get() -> None:
    cache = FakeCache()
    cache.set("user:1", "Yosri")

    assert cache.get("user:1") == "Yosri"


def test_get_missing_key() -> None:
    cache = FakeCache()

    assert cache.get("missing") is None


def test_incr() -> None:
    cache = FakeCache()

    assert cache.incr("requests") == 1
    assert cache.incr("requests") == 2
