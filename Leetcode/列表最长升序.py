# def longest_up(li):
#     target = 0
#     dict1 = dict()
#     li2 = list()
#     for i, n in enumerate(li):
#         if i + 1 < len(li):
#             if target < n < li[i + 1]:
#                 target = n
#                 li2.append(n)
#             else:
#                 target = n
#                 dict1.update({len(li2): list(li2)})
#                 li2.clear()
#         else:
#             if target < n:
#                 li2.append(n)
#                 dict1.update({len(li2): li2})
#                 return dict1.get(max(dict1))
#
#
# a = longest_up([9, 3, 4, 1, 2, 5, 6, 8, 9, 14, 11, 25, 35, ])
# print(a)

# def longest_up2(li):
#     li1 = list()
#     dict1 = dict()
#     for i, n in enumerate(li):
#         target = n
#         li1.append(n)
#         for nu in li[i:]:
#             if nu > target:
#                 li1.append(nu)
#                 target = nu
#         print(li1)
#         if len(li1) in dict1:
#             dict1.update({len(li1): list([dict1.setdefault(len(li1)), list(li1)])})
#         else:
#             dict1.update({len(li1): list(list(li1))})
#         li1.clear()
#         print(dict1)
#
#     return dict1.get(max(dict1))
#
#
# a = longest_up2([2, 1, 5, 2, 4, 5, 1, 3, 7, 9, 7, 8, 12, 20])
# print(a)


# def split_list(li):
#     if len(li) <= 1:
#         return li
#     else:
#         left = li[:len(li) // 2]
#         right = li[len(li) // 2:]
#         return left, right
#
#
# def longest_up(l, r):
#
#
#
#     return
#
#
# split_list([2, 1, 5, 2, 4, 5, 1, 3, 7, 9, 7, 8, 12, 20])
