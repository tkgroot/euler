# Project Euler Task 1
# @author tkgroot
#


def main(limit):
    sum = 0
    idx = 0

    while idx < limit:
        if idx % 3 == 0 or idx % 5 == 0:
            sum += idx
            idx += 1

    return sum


if __name__ == '__main__':
    print(main(1000))
