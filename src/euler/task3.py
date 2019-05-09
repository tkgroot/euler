"""
Project Euler Task3 - Largest prime factor.

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math


def factor(num):
    """Factorize."""
    factorArray = []
    for x in range(3, num):
        if num % x == 0 and isPrime(x):
            factorArray.append(x)
    print(factorArray)
    return factorArray


def max_factor(num):
    """Maximum Factor."""
    return max(factor(num))


def isPrime(num):
    """Determine if number is a prime number."""
    if num % 2 == 0:
        return False
    for x in range(3, int(math.sqrt(num)) + 1, 2):
        if num % x == 0:
            return False
    return True


def main():
    """main."""
    # print(4 % 2)
    factor(1475143)
    # print(max_factor(600851475143))


if __name__ == "__main__":
    main()
