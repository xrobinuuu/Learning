def sortArrayByParity(nums):
    # ls1 = list()
    # ls2 = list()
    # for i in nums:
    #     if divmod(i, 2)[1]:
    #         ls1.append(i)
    #     else:
    #         ls2.append(i)
    # ls2.extend(ls1)
    # return ls2

    if not nums:
        return []
    n = nums[:1]
    if n[0] % 2:
        return sortArrayByParity(nums[1:]) + [n]
    return [n] + sortArrayByParity(nums[1:])

    # dup = list()
    # while nums:
    #     n = nums[:1]
    #     if n[0] % 2:
    #         dup.extend(n)
    #     else:
    #         n.extend(dup)
    #         dup = n
    #     nums = nums[1:]
    # return dup


if __name__ == "__main__":
    Nums = [1, 0, 3]
    x = sortArrayByParity(Nums)
    print(x)
