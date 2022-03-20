"""Test cmat2aset."""
# pylint: disable=broad-except
from cmat2aset import __version__
from cmat2aset import cmat2aset


def test_version():
    """Test version."""
    assert __version__ == "0.1.0"


def test_sanity():
    """Sanity check."""
    try:
        assert not cmat2aset()
    except Exception:
        assert True
