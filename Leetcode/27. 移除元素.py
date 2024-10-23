def removeElement(nums: list, val: int):
    cot = nums.count(val)
    for i in range(cot):
        nums.remove(val)
    return len(nums)


if __name__ == "__main__":
    Nums = [0, 1, 2, 2, 3, 0, 4, 2]
    Val = 2
    y = removeElement(Nums, Val)
    print(y)

