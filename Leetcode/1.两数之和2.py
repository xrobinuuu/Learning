import time

t1 = time.perf_counter()


def twoSum(nums, target):
    for k, num in enumerate(nums):
        a = nums[:k + 1]
        b = nums[k + 1:]
        print(a, b)
        for v, new_num in enumerate(b):
            if a[-1] + new_num == target:
                print([k, (a.index(a[-1]) + v + 1)])
                return [k, (a.index(a[-1]) + v + 1)]


twoSum([3, 3, 6, 7], 10)
t2 = time.perf_counter()
print(t2 - t1)
