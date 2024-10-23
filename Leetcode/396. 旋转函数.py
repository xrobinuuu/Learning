import numpy


def maxRotateFunction(nums: list[int]) -> int:
    # right = list()
    # for i in range(len(nums)):
    #     nums.append(nums.pop(0))
    #     right.append(copy.deepcopy(nums))
    # right = numpy.array(right)

    return int(max([numpy.dot(numpy.roll(numpy.array(nums), i), numpy.arange(len(nums))) for i in range(len(nums))]))


if __name__ == "__main__":
    Nums = [4, 3, 2, 6]
    x = maxRotateFunction(Nums)
    print(x)
