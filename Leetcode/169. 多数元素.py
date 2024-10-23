def majorityElement(nums):
    # cot, num = 0, None
    # for v in nums:
    #     if cot == 0:
    #         num = v
    #     cot += 1 if num == v else -1
    # return num

    cot, num = 0, nums[0]
    for v in nums:
        if cot == 0:
            num = v
        if num == v:
            cot += 1
        else:
            cot -= 1

    return num


if __name__ == "__main__":
    Nums = [3, 2, 3]
    y = majorityElement(Nums)
    print(y)
