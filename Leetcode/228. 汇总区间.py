def summaryRanges(nums: list[int]) -> list[str]:
    if len(nums) < 2:
        return list(map(str, nums))
    n = nums[0]
    ls = [str(n)]
    for i, v in enumerate(nums[1:], 1):
        if v - nums[i - 1] == 1:
            continue
        ls[-1] += "" if n == nums[i - 1] else ("->%d" % nums[i - 1])
        ls.append(str(v))
        n = v
    if nums[-1] - nums[-2] == 1:
        ls[-1] = ls[-1] + "->" + str(nums[-1])
    return ls


if __name__ == '__main__':
    Nums = [0, 2, 3, 4, 6, 8, 9]
    y = summaryRanges(Nums)
    print(y)
