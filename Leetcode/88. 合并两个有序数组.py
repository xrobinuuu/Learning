def merge(nums1, m: int, nums2, n: int):
    for i in range(m):
        nums1[i + n] = nums2[i]
    nums1.sort()


if __name__ == "__main__":
    Nums1 = [1, 2, 3, 0, 0, 0]
    M = 3
    Nums2 = [2, 5, 6]
    N = 3
    merge(Nums1, M, Nums2, N)
