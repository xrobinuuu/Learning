def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    s = set()
    for i, v in enumerate(nums):
        if i > k:
            s.remove(nums[i - k - 1])
        if v in s:
            return True
        s.add(v)
    return False


if __name__ == "__main__":
    Nums = [1, 2, 3, 1]
    K = 2
    x = containsNearbyDuplicate(Nums, K)
    print(x)
