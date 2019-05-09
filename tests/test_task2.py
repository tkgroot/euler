"""Test Task2."""
from src.euler import task2 as fibonacci


def test_fibo():
    """
    Validate that the fibonacci.fibo function.

    It should return the correct number of the element´s position in the fibonacci
    sequence.
    """
    assert fibonacci.fibo(9) == 34
    assert fibonacci.fibo(10) == 55
    assert fibonacci.fibo(11) == 89


def test_sum_fibo():
    """Validate the sum of the even-valued terms."""
    assert fibonacci.calculate_sum(10) == 10
    # assert fibonacci.calculate_sum(11) == 10
    assert fibonacci.calculate_sum(40) == 44
    # assert fibonacci.calculate_sum(50) == 44
