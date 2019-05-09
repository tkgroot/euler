"""
Project Euler Task 4 - Largest palindrome product.

A palindromic number reads the same both ways. The largest palindrome made from the
product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import numpy as np


def palindrome(num):
    """
    Determine if the number is a palindrome.

    :param num: number to evaluate
    :return: ``true`` if number is a palindrome or ``false`` if not.
    """
    rev_num = int(str(num)[::-1])
    if num == rev_num:
        return True
    return False


def main(num_digits):
    """
    Find the largest palindrome for the number of digits.

    :param num_digits: the amount of digits
    :return: the palindrome for the amount of digits passed
    """
    pd_range = []
    if num_digits == 2:
        pd_range = np.arange(10, 100)
    elif num_digits == 3:
        pd_range = np.arange(100, 1000)

    result = []  # np.zeros(pd_range.size, dtype=int)
    for idx in pd_range:
        for kdx in pd_range:
            if palindrome(kdx * idx):
                result.append(kdx * idx)

    return max(result)


if __name__ == "__main__":
    print(main(3))
