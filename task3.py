# Project Euler Task 3
# @author tkgroot
#
import math


def factor(num):
    factorArray = []
    for x in range(3, num):
        if num % x == 0 and isPrime(x):
            factorArray.append(x)
    print(factorArray)
    return factorArray


def max_factor(num):
    return max(factor(num))


def isPrime(num):
    if num % 2 == 0:
        return False
    for x in range(3, int(math.sqrt(num)) + 1, 2):
        if num % x == 0:
            return False
    return True


def main():
    # print(4 % 2)
    factor(1475143)
    # print(max_factor(600851475143))


if __name__ == '__main__':
    main()
