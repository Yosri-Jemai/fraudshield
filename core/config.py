# Reads application settings from environment variables.

import os


class Settings:
    def __init__(self):
        self.cache_backend = os.getenv("CACHE_BACKEND", "memory").lower()


def get_settings() -> Settings:
    """Return the application settings."""
    return Settings()
