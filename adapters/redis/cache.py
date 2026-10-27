import os

from redis import Redis


class RedisCache:
    """Redis implementation of the CacheStore port."""

    def __init__(self, url: str | None = None) -> None:
        self.client: Redis = Redis.from_url(
            url
            or os.getenv(
                "REDIS_URL",
                "redis://localhost:6379/0",
            ),
            decode_responses=True,
        )

    def get(self, key: str) -> str | None:
        return self.client.get(key)

    def set(
        self,
        key: str,
        value: str,
        ttl: int | None = None,
    ) -> None:
        self.client.set(key, value, ex=ttl)

    def incr(self, key: str) -> int:
        return self.client.incr(key)

    def close(self) -> None:
        self.client.close()
