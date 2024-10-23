import math
import random
import time
import queue


# def poor_glass(num1, num2, target):
#     '''cT = z'''
#     if num1 + num2 < target:
#         return False
#     if num1 == 0 or num2 == 0:
#         return num1 + num2 == target
#     while num1 % num2:
#         num1, num2 = num2, num1 % num2
#     return target % num2 == 0
#
#
# def test(num1, num2):
#     while num1 % num2:
#         num1, num2 = num2, num1 % num2
#     return num2
#
#
# if __name__ == "__main__":
#     # result = bad_glass(11, 13, 1)
#     # result = poor_glass(3, 5, 8)
#     # print(result)
#     ls = [random.randint(1, 10000) for i in range(1000000)]
#     for i in range(len(ls) - 1):
#         if test(ls[i], ls[i+1]) != math.gcd(ls[i], ls[i + 1]):
#             print(ls[i], ls[i + 1])


# class PoorBuker:
#     def __init__(self, a, b, z):
#         self.a_volume = a
#         self.b_volume = b
#
#         self.a = 0
#         self.b = 0
#         self.status = [[0, 0]]
#         self.current_status = list()
#         self.check()
#
#     def a_full(self):
#         self.a = self.a_volume
#
#     def b_full(self):
#         self.b = self.b_volume
#
#     def a_clear(self):
#         self.a = 0
#
#     def b_clear(self):
#         self.b = 0
#
#     def a_to_b(self):
#         if self.a + self.b < self.b_volume:
#             self.b = self.a + self.b
#             self.a_clear()
#             self.rec_ststus()
#             self.a_full()
#             self.rec_ststus()
#         else:
#             self.a = self.a - self.b_volume + self.b
#             self.b_full()
#             self.rec_ststus()
#         self.check()
#
#     def b_to_a(self):
#         if self.a + self.b < self.a_volume:
#             self.a = self.a + self.b
#             self.b_clear()
#             self.rec_ststus()
#             self.b_full()
#             self.rec_ststus()
#         else:
#             self.b = self.b - self.a_volume + self.a
#             self.a_full()
#             self.rec_ststus()
#         self.check()
#
#     def rec_ststus(self):
#         self.current_status = [self.a, self.b]
#         self.status.append([self.a, self.b])
#
#     def check(self):
#         if self.current_status in self.status:
#
#         if self.a == 0 and self.b == 0:
#             if self.a_volume > self.b_volume:
#                 self.a_full()
#             else:
#                 self.b_full()
#         if self.b == self.b_volume:
#             self.b_to_a()
#         if self.a == self.a_volume:
#             self.a_to_b()
#
#
#
# if __name__ == "__main__":
#     ps = PoorBuker(3, 5, 8)
#     a, b = ps.check()
#     print(a, b)


# def big_to_small():
#     global big, small, current_status
#     if big == big_volume:
#         big = big - samll_volume + small
#         small = samll_volume
#         current_status = tuple([big, small])
#     find_check()
#
#
# def small_to_big():
#     global big, small, current_status
#     if small == samll_volume:
#         small = small - big_volume + big
#
#         current_status = tuple([big, small])

# status = set()
# current_status = tuple()
# q_status = queue.LifoQueue()
# big = 0
# small = 0
# big_volume = 5
# samll_volume = 3
#
#
# def find_check(target):
#     global big, small, current_status, q_status, status
#     if big == 0 and small == 0:
#         big = big_volume
#         current_status = current_status = tuple([big, small])
#         status.add(current_status)
#         status.add((0, samll_volume))
#
#     if big == big_volume:
#         big = big - samll_volume + small
#         small = samll_volume
#         current_status = tuple([big, small])
#     if small == samll_volume:
#         if big + small > big_volume:
#             small = big + small - big_volume
#             big = big_volume
#         else:
#             big = big + small
#             small = 0
#         current_status = tuple([big, small])
#
#     if current_status not in status:
#         q_status.put(current_status)
#     if q_status.empty():
#         return False
#     for i in range(q_status.qsize()):
#         a, b = q_status.get_nowait()
#         if a + b == target:
#             return True
#     return find_check(target)


def find_status(x, y, z):
    status_ls = [(0, 0)]
    history_status = set()
    while status_ls:
        status_now = status_ls.pop()
        if status_now in history_status:
            continue
        history_status.add(status_now)
        temp_x = status_now[0]
        temp_y = status_now[1]
        if temp_x + temp_y == z:
            return True
        status_ls.append((temp_x, 0))
        status_ls.append((0, temp_y))
        status_ls.append((x, temp_y))
        status_ls.append((temp_x, y))
        status_ls.append((temp_x - min(y - temp_y, temp_x), temp_y + min(y - temp_y, temp_x)))
        status_ls.append((temp_x + min(x - temp_x, temp_y), temp_y - min(x - temp_x, temp_y)))
    return False


if __name__ == "__main__":
    # a = find_check(target=4)
    # print(a)

    # res = find_status(3, 5, 4)
    # print(res)
    ls = '123'
    res = ls.replace('2', '3')
    print(id(res))
    print(res)