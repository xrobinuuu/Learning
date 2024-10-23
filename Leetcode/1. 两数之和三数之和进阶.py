import random
import time


# li1 = [random.randrange(1, 100, ) for i in range(10)]
# # li1 = [37, 95, 95, 73, 49, 66, 70, 53, 91, 16, 39, '/']
#
# # for index in li1:
# #     if not str(index).isdigit():
# #         li1.remove(index)
# # list2 = list(set(li1))
# #
# # for i in range(3):
# #     num = max(list2)
# #     list2.remove(num)
# # print(num)
#
# # 第二题
#
# # lia = [1, 2, 3, 4, 45, 66, 70, 53, 91, 16, 39, ]
#

#
# # dict1 = dict()
# #
# #
# # def TwoSUum(x, ls):
# #     for i in lia:
# #         if x + i == 6 and (x != i):
# #             return True
# #
# #
# # for ind in filter(TwoSUum, lia, args=(lia, )):
# #     print(lia.index(ind))
#
# #


#
#


def twoSum(nums, target):
    dict1 = dict()
    for i, n in enumerate(nums):
        if target - n in dict1:
            return nums[i], nums[dict1[target - n]]
        dict1.update({n: i})


t1 = time.perf_counter()
a, b = twoSum([3, 3, 6, 7, 10], 17)
t2 = time.perf_counter()
print(a, b, t2 - t1)


# def threeSum(nums, target):
#     dict1 = dict()
#     for i, n in enumerate(nums):
#         num1 = target - n
#         if num1 in dict1:
#             return i, list(dict1[num1].items())
#         dict1.update({num1: {dict1.get(target): i}})
#         print(dict1)
#
#
# a, b = threeSum([3, 3, 6, 7, 10], 23)
# print(a, b)

# dict1 = dict()

def threeSum(nums, target, dic: dict, cot=0):
    """

    @type dic: object
    """
    sec_target = target - nums[cot]
    for i, n in enumerate(dic.keys()):
        if sec_target - n in dic:
            return "+".join([str(n), str(nums[cot]), str(sec_target - n)]) + "=" + str(target)
    dic.update({nums[cot]: cot})
    cot += 1
    return threeSum(nums, target, dic, cot)


t21 = time.perf_counter()
a= threeSum([3, 4, 6, 7, 10, 20], 33, {}, 0)
t22 = time.perf_counter()
print(a, t22 - t21)
