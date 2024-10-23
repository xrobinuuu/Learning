def numSubarrayProductLessThanK(nums, k: int):
    ind, cot, target = 0, 0, 1
    # for i, v in enumerate(nums):
    #     target *= v
    #     while target >= k and i >= ind:
    #         target //= nums[ind]
    #         ind += 1
    #     cot += i - ind + 1
    # return cot


if __name__ == "__main__":
    Nums = [10, 5, 2, 6]
    K = 0
    y = numSubarrayProductLessThanK(Nums, K)
    print(y)
