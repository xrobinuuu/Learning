from typing import List
import numpy as np


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        grid_list = list()
        total = (n ** 2) * ((n ** 2) + 1) // 2
        for row in grid:
            for col in row:
                grid_list.append(col)
        b = sum(set(grid_list))
        return [sum(grid_list) - b, total - b]

    def findMissingAndRepeatedValues2(self, grid: List[List[int]]) -> List[int]:
        arr = np.array(grid)
        grid_sum = arr.sum()
        unique_sum = np.unique(arr).sum()
        size = arr.size
        total = size * (size + 1) // 2
        return [grid_sum - unique_sum, total - unique_sum]

    def findMissingAndRepeatedValues3(grid: List[List[int]]) -> List[int]:
        c = Counter(x for r in grid for x in r)
        d = {c[i]: i for i in range(1, len(grid) ** 2 + 1)}
        return [d[2], d[0]]



if __name__ == '__main__':


    def findMissingAndRepeatedValues(grid: List[List[int]]) -> List[int]:
        c = Counter(x for r in grid for x in r)
        d = {c[i]: i for i in range(1, len(grid) ** 2 + 1)}
        return [d[2], d[0]]


    f = open("user.out", "w")
    a = 0
    for case in map(loads, stdin):
        for i in range(2):
            if a == 0:
                b = case
                a += 1
            else:
                print(str(findMissingAndRepeatedValues(b)).replace(", ", ","), file=f)
                a = a - 1
    exit(0)

