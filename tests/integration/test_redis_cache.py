import uuid

import pytest
from redis import Redis
from redis.exceptions import RedisError

from adapters.redis.cache import RedisCache


@pytest.fixture
def cache():
    url = "redis://localhost:6379/0"
    client = Redis.from_url(url)

    try:
        client.ping()
    except RedisError:
        client.close()
        pytest.skip("Redis is not running")

    client.close()
    instance = RedisCache(url)
    yield instance

    instance.client.close()


def test_set_and_get(cache):
    key = f"test:{uuid.uuid4()}"
    cache.set(key, "hello")

    assert cache.get(key) == "hello"


def test_get_missing_key(cache):
    assert cache.get(f"test:{uuid.uuid4()}") is None


def test_increment(cache):
    key = f"test:{uuid.uuid4()}"

    assert cache.incr(key) == 1
    assert cache.incr(key) == 2


def test_set_with_ttl(cache):
    key = f"test:{uuid.uuid4()}"
    cache.set(key, "temporary", ttl=60)

    assert cache.get(key) == "temporary"
    assert cache.client.ttl(key) > 0
