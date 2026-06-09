"""basic_math — minimal pybind11 example package."""

# Re-export the compiled C++ extension so callers can simply write:
#   from basic_math import add
# instead of importing the internal extension module directly.
from .basic_math import add  # noqa: F401

try:
    from ._version import version as __version__
except ImportError:
    # Package has not been installed; version unknown.
    __version__ = "unknown"

__all__ = ["add"]
