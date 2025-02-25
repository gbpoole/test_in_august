from importlib import metadata  # make sure to import metadata explicitly

__version__ = metadata.version(__package__ or __name__)


class BaseException(Exception):
    """Base class for exceptions raised from test_in_august"""

    def __init__(self, message: str):
        self._message = message

    def __str__(self) -> str:
        return f"{self._message}"
