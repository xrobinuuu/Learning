import copy
from typing import List


class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        result = 2 ** 32
        for aliceIndex in range(len(nums)):
            maxChanges2 = copy.deepcopy(maxChanges)
            temp = copy.deepcopy(nums)
            k_count = 0
            work = 0
            while k_count < k:
                if temp[aliceIndex] == 1:
                    temp[aliceIndex] = 0
                    k_count += 1
                elif (aliceIndex + 1 < len(nums) and temp[aliceIndex + 1] == 1):
                    temp[aliceIndex], temp[aliceIndex + 1] = temp[aliceIndex + 1], temp[aliceIndex]
                    work += 1
                elif (aliceIndex - 1 >= 0 and temp[aliceIndex - 1] == 1):
                    temp[aliceIndex], temp[aliceIndex - 1] = temp[aliceIndex - 1], temp[aliceIndex]
                    work += 1
                elif maxChanges2 > 0 and aliceIndex + 1 < len(nums):
                    temp[aliceIndex + 1] = 1
                    maxChanges2 -= 1
                    work += 1
                elif maxChanges2 > 0 and aliceIndex - 1 > len(nums):
                    maxChanges2 -= 1
                    temp[aliceIndex + 1] = 1
                    work += 1
                else:
                    work = 2 ** 32
                    break
            print(work)
            result = min(result, work)
        return result


_nums = [1, 0, 1, 0, 1]
_k = 3
_maxChanges = 0
r = Solution().minimumMoves(_nums, _k, _maxChanges)
print(r)
