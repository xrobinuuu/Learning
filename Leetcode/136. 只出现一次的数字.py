def singleNumber(nums):
    num = nums.pop()
    while nums:
        num ^= nums.pop()
    return nums


if __name__ == "__main__":
    Num = [4, 1, 2, 1, 2]
    singleNumber(Num)
