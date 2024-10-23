from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        count = 0
        pointer = 0
        end = len(nums) - 1
        init_num = nums[0] + nums[1]
        while pointer < end and (nums[pointer] + nums[pointer + 1]) == init_num:
            count += 1
            pointer += 2
        return count


_nums = [3, 2, 1, 4, 5]
result = Solution().maxOperations(_nums)
print(result)
