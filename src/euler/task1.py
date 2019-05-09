"""
Project Euler Task 1 - Multiples of 3 and 5.

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6
and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def main(limit):
    """
    Find the sum of all multiples of 3 or 5.

    :param limit: numerical upper limit
    :return: sum of multiples of 3 or 5 below the upper limit passed
    """
    sum = 0
    idx = 0

    while idx < limit:
        if idx % 3 == 0 or idx % 5 == 0:
            sum += idx
            idx += 1

    return sum


if __name__ == "__main__":
    print(main(1000))
