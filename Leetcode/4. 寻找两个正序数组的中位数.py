from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length1 = len(nums1)
        length2 = len(nums2)
        div, mod = divmod(length1 + length2, 2)
        i = 0
        j = 0
        target = 0
        last_target = 0
        while i + j <= div:
            last_target = target
            if (j >= length2) or (i < length1 and nums1[i] <= nums2[j]):
                target = nums1[i]
                i += 1
            else:
                target = nums2[j]
                j += 1
        if mod == 1:
            return float(target)
        return (target + last_target) / 2.0

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        div, mod = divmod(len(nums1) + len(nums2), 2)
        nums = sorted(nums1 + nums2)
        if mod == 1:
            return float(nums[div])
        return (nums[div - 1] + nums[div]) / 2.0


_nums1 = [1]
_nums2 = [3]
result = Solution().findMedianSortedArrays(_nums1, _nums2)
print(result)
