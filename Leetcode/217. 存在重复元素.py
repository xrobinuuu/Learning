def containsDuplicate(nums: list[int]) -> bool:
    return len(set(nums)) != len(nums)