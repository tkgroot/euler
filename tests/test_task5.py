# Project Euler Test for Task 5
# @ author tkgroot
#
from src.euler import task5


def test_even_divide():
    assert task5.main(10) == 2520
