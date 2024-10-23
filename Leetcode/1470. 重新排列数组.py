def insrt(nums, n):
    # li = list()
    # for i in range(n):
    #     li.append(nums[:n][i])
    #     li.append(nums[n:][i])
    # return li
    for i in range(1, n):

        j = nums[i]
        k = nums[n]
        nums[i] = k
        nums[n] = nums[n + 1]
        nums[n + 1] = j

    return nums


if __name__ == "__main__":
    Nums = [2, 5, 1, 3, 4, 7]
    N = 3
    x = insrt(Nums, N)
    print(x)
