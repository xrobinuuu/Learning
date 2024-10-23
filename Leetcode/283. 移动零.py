def moveZeroes(nums: list[int]) -> None:
    cot = nums.count(0)
    for i in range(cot):
        nums.remove(0)
    nums.extend([0, ] * cot)
    print(nums)


Nums = [0, 1, 0, 3, 12]
moveZeroes(Nums)

print(bin(20))
