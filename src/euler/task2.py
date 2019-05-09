# Project Euler Task 2
# @author tkgroot
#
num_dict = {0: 0, 1: 1}


def fibo(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    try:
        if num_dict[x]:
            return num_dict[x]
    except:
        return fibo(x - 1) + fibo(x - 2)


def calculate_sum(limit):
    sum, idx = 0, 0

    while list(num_dict.values())[-1] < limit:
        # if idx % 1000 == 0:
        #     print('{} done'.format(idx))
        num_dict[idx] = fibo(idx)

        if num_dict[idx] % 2 == 0:
            sum += num_dict[idx]
        idx += 1
    return sum


def main():
    print(calculate_sum(4000000))


if __name__ == '__main__':
    main()
