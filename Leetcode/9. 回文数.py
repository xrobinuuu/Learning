# class Solution:
#     def isPalindrome(self, x):
#         y = int(str(x).strip("-")[::-1])
#         if str(x).startswith("-"):
#             self.ret(-1*y, x)
#         else:
#             self.ret(y, x)
#
#     def ret(self, y, x):
#         if y == x:
#             return print(True)
#         else:
#             return print(False)
#
#
# Solution().isPalindrome(121)
# class Solution:
#     def isPalindrome(self, x):
#         x = str(x)
#         y = x[::-1]
#         if y == x:
#             return True
#         else:
#             return False


# def ret(y, x):
#     if y == x:
#         return True
#     else:
#         return False
#
#
# def test(x):
#     y = int(str(x).strip('-')[::-1])
#     if str(x).startswith("-"):
#         return ret(-y, x)
#     else:
#         return ret(y, x)
#
#
# print(test(121))
#
#
# def foo():
#     return True
#
#
# print(foo())