# Project Euler Task 5
# @author tkgroot
#
import numpy as np


def main(limit):
    if limit == 10:
        dividers = np.arange(1, limit + 1)[::-1]
    else:
        dividers = np.arange(11, limit + 1)[::-1]
    res = limit
    stop = 1

    print(dividers)
    while stop < (10 - 1):
        for divider in dividers:
            # print(res, divider, res % divider, stop)
            if res % divider != 0:
                stop = 1
                break
            else:
                stop += 1
        if stop > 8: print('stop {} at {}'.format(stop, res))
        res += 1
        if res % 10000000 == 0: print('{} done.'.format(res))
    return res - 1


if __name__ == '__main__':
    print(main(20))
