from collections import Counter


class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        # def huisuo(num,k,digits):
        result, ct = [], Counter(digits)
        print(ct)

        def recur(num=0):
            if num >= 100:
                return result.append(num)
            for i in (range(10) if num < 10 else range(0, 9, 2)):
                if ct[i]:
                    ct[i] -= 1
                    (num or i) and recur(num * 10 + i)
                    ct[i] += 1

        return recur() or result


a = Solution().findEvenNumbers([1, 2, 3, 4, 5, 8])
print(a)
