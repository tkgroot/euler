"""Poetry initial Package Test."""
from src.euler import __version__


def test_version():
    """Validate the package version."""
    assert __version__ == '0.1.0'
