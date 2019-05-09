# Project Euler Task 4
# @author tkgroot
#
import numpy as np


def palindrome(num):
    rev_num = int(str(num)[::-1])
    if num == rev_num:
        return True
    return False


def main(num_digits):
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


if __name__ == '__main__':
    print(main(3))
