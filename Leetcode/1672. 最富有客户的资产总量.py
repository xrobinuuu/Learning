import numpy


def maximumWealth(accounts: list[list[int]]) -> int:
    # if not accounts:
    #     return 0
    # max_num = 0
    # while accounts:
    #     max_num = max(sum(accounts.pop()), max_num)
    # return max_num

    # return int(max(numpy.sum(accounts, axis=1)))

    max_num = 0
    for i in accounts:
        max_num = max(sum(i), max_num)
    return max_num


if __name__ == "__main__":
    accounts = [[1, 2, 3], [3, 2, 1]]
    x = maximumWealth(accounts)
    print(x)
