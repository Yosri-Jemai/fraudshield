from typing import Protocol


class CacheStore(Protocol):
    """Interface for a key-value cache."""

    def get(self, key: str) -> str | None:
        """Return the value for a key, or None if it doesn't exist."""
        ...

    def set(self, key: str, value: str, ttl: int | None = None) -> None:
        """Store a value, optionally expiring it after ttl seconds."""
        ...

    def incr(self, key: str) -> int:
        """Increment a counter and return its new value."""
        ...
