from itertools import combinations
from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:

        return max(prices[0], prices[] - prices[-2])

    def max_profit4(self, prices: List[int]) -> int:
        max_price = 0
        for i in range(len(prices) - 1):
            max_price = max(max_price, max(prices[i + 1:]) - prices[i])
        return max_price

    def max_profit2(self, prices: list[int]) -> int:
        b = list(map(lambda a: a[1] - a[0], combinations(prices, 2)))
        return max(b) if len(prices) > 1 and max(b) > 0 else 0

    def max_profit3(self, prices: list):
        target = 0
        i = 1
        while len(prices) > i:
            subtract = prices[i] - prices[i - 1]
            if subtract > 0:
                target = max(subtract, target)
                prices[i], prices[i - 1] = prices[i - 1], prices[i]
            i += 1

        return target


if __name__ == "__main__":
    ls = [7, 6, 9, 3, 8, 1]
    Solution().max_profit(ls)
