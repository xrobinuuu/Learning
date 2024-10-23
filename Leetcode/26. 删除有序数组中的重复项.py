def removeDuplicates(nums):
    j = k = 1
    ex = len(nums)
    while j < ex:
        if nums[j] != nums[j - 1]:
            nums[k] = nums[j]
            k += 1
        j += 1


if __name__ == "__main__":
    Nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    removeDuplicates(Nums)
