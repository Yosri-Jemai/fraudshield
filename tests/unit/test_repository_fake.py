from adapters.fakes.repository import FakeRepository


def test_save_and_get():
    repo = FakeRepository()
    repo.save("tx1", {"amount": 100})

    assert repo.get("tx1") == {"amount": 100}


def test_get_missing_record():
    repo = FakeRepository()

    assert repo.get("unknown") is None


def test_delete_record():
    repo = FakeRepository()
    repo.save("tx1", {"amount": 100})
    repo.delete("tx1")

    assert repo.get("tx1") is None
