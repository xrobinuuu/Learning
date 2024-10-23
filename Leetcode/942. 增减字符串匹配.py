from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        a = 0
        b = len(s)
        s += s[-1]
        res = list()
        for i in s:
            if i == "I":
                res.append(a)
                a += 1

            else:
                res.append(b)
                b -= 1
        return res