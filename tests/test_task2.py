from src.euler import task2 as fibonacci


def test_fibo():
    assert fibonacci.fibo(9) == 34
    assert fibonacci.fibo(10) == 55
    assert fibonacci.fibo(11) == 89


def test_sum_fibo():
    assert fibonacci.calculate_sum(10) == 10
    # assert fibonacci.calculate_sum(11) == 10
    assert fibonacci.calculate_sum(40) == 44
    # assert fibonacci.calculate_sum(50) == 44
