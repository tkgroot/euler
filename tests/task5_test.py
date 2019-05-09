"""Test Task5."""
from src.euler import task5


def test_even_divide():
    """Validate even_divide function.

    2520 is the smallest number that can be divided by each of the numbers from 1 to 10
    without any reminder.
    """
    assert task5.main(10) == 2520
