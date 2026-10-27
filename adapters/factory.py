# Creates the cache implementation selected by the configuration.

from adapters.fakes.cache import FakeCache
from core.config import get_settings


def create_cache() -> FakeCache:
    """Create the configured cache implementation."""
    settings = get_settings()

    if settings.cache_backend == "memory":
        return FakeCache()

    raise ValueError(f"Unsupported cache backend: {settings.cache_backend}")
