def isMonotonic(nums: list[int]) -> bool:
    return sorted(nums) == nums or sorted(nums) == nums[::-1]