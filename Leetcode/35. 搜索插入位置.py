def searchInsert(nums: list[int], target: int):
    r = len(nums) - 1
    ind = 0
    while ind <= r:
        flat = (ind + r) // 2
        if nums[flat] == target:
            return flat
        elif nums[flat] > target:
            r = flat - 1
        else:
            ind = flat + 1
    return ind


if __name__ == "__main__":
    Nums = [1, 3, 5, 6]
    Target = 2
    y = searchInsert(Nums, Target)
    print(y)
