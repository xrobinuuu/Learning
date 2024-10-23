# def sp(n):
#     def consecutiveNumbersSum(ls, r):
#         q = list()
#         target = ls[0] // 2
#         for val in ls:
#             m = divmod(val, 2)
#             j, k = m[0], m[0] + 1
#             if j < 3 or k < 3:
#                 r += 1
#                 return [1, q]
#             elif target == j:
#                 q.append(j)
#                 q.append(k)
#                 target = k + 1
#
#         return [1, q]
#         # print(num)
#         # if n <= 2: return
#         # m = divmod(num, 2)
#         # j, k = m[0], m[0] + 1
#         # if not m[1] and k > 2:
#         #     j, k = m - 1, k + 1
#         # if j not in h and k not in h:
#         #     print("res", res)
#         #     history.append(j)
#         #     history.append(k)
#         #     q.append(j)
#         #     q.append(k)
#         #     r += 1
#
#     que = [n]
#     res = 1
#     while que:
#         x = consecutiveNumbersSum(que, res)
#         que = x[1]
#         res += x[0]
#     return res


# if __name__ == "__main__":
#     N = 15
#     y = sp(N)
#     print(y)
