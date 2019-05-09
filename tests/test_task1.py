"""Test Task1."""
from src.euler import task1 as multiply


def test_multiply():
    """Validate that the multipliers of 3 or 5 below 10 is equal to 23."""
    assert multiply.main(10) == 23
