import re

# def is_valid(s: str):
#     valid_map = {
#         '(': ')',
#         '[': ']',
#         '{': '}',
#     }
#
#     if (len(s) % 2 != 0) or (not s):
#         return False
#     stock = []
#     index = 0
#     while index < len(s):
#         left = s[index]
#         if left in valid_map.keys():
#             if valid_map[left] == s[index + 1]:
#                 pass
#             else:
#                 stock.append(s[index])
#         else:
#             return False
#     return True
#
#
# if __name__ == "__main__":
#     print(is_valid("[()({)[]])}"))

from operator import itemgetter

cost = [1]
x = itemgetter(*[i for i in range(len(cost)) if i % 3 != 2])(sorted(cost, reverse=True))
print(x)
