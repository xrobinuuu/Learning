def findDuplicates(nums: list[int]) -> list[int]:
    # ex = len(nums)
    # ind = 0
    # res = list()
    # while ind < ex:
    #     j = nums[ind]
    #     k = nums[j - 1]
    #     if not j ^ k == j:
    #
    #
    #     res.append(k)

    # if nums[0] == 1:
    # i = 0
    # res = list()
    # while i < len(nums):
    #     t = abs(nums[i])
    #     if nums[t - 1] < 0:
    #         res.append(t)
    #     nums[t - 1] = -nums[t - 1]
    #     i += 1
    # return res

    # lt = len(nums)
    # for i in range(lt):
    #     while nums[i] != nums[nums[i] - 1]:
    #         nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    #
    # print(nums)
    # return [num for i, num in enumerate(nums) if num - 1 != i]

    nums.sort()
    ls = []
    for i, num in enumerate(nums[1:], 1):
        if num == nums[i - 1]:
            ls.append(num)
    return ls


if __name__ == '__main__':
    Nums = [4, 3, 2, 7, 8, 2, 3, 1]
    y = findDuplicates(Nums)
    print(y)
