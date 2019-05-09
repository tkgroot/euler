"""Test Task3."""
import src.euler.task3 as pf
import pytest


def test_prime():
    """Validate isPrime function returns correct values."""
    test = {
        3: True,
        4: False,
        5: True,
        6: False,
        7: True,
        8: False,
        9: False,
        10: False,
        11: True,
        12: False,
        13: True,
        14: False,
        15: False,
    }
    for key, val in test.items():
        assert pf.isPrime(key) == val


def test_pf():
    """Validate the prime factor function."""
    assert pf.factor(13195) == [5, 7, 13, 29]


def test_max_pf():
    """Validate the prime max_factor function."""
    assert pf.max_factor(13195) == 29


@pytest.mark.timeout(10)
def test_time_max_pf():
    """Validate the max_factor function with time constraint."""
    pf.max_factor(851475143)
