"""A tiny example package demonstrating Python packaging."""

from importlib.metadata import PackageNotFoundError, version

from foundit_hello.greeter import Hello

try:
    __version__ = version("foundit-hello")
except PackageNotFoundError:
    __version__ = "0.0.0"


__all__ = ["Hello"]
