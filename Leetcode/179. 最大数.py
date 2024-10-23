from itertools import permutations


def largestNumber(nums):
    # def merge_nums(nums: list):
    #     # return str(int(max(map(lambda a: "".join(a), permutations(map(str, nums))))))

    #     if len(nums) < 2:
    #         return nums
    #     left = list()
    #     right = list()
    #     position_arg = nums.pop(0)
    #     for num in nums:
    #         j = position_arg * pow(10, len(str(num))) + num
    #         k = num * pow(10, len(str(position_arg))) + position_arg
    #         if j < k:
    #             left.append(num)
    #         else:
    #             right.append(num)
    #     return merge_nums(left) + [position_arg] + merge_nums(right)
    # return str(int("".join(map(str, merge_nums(nums)))))

    gap = 1
    while gap < (len(nums) / 3):
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, len(nums)):
            temp = nums[i]
            j = i - gap
            while j >= 0 and str(temp) + str(nums[j]) > str(nums[j]) + str(temp):
                nums[j + gap] = nums[j]
                j -= gap
            nums[j + gap] = temp
        gap = divmod(gap, 3)[0]
    return str(int("".join(map(str, nums))))


if __name__ == "__main__":
    Nums = [3, 30, 34, 5, 9]
    # Nums = [0, 0]
    x = largestNumber(Nums)
    print(x)
