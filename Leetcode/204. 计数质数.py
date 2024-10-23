import math
import time
import numpy as np
from numba import njit, jit


def count_primes(n: int):
    if n < 5:
        if n < 3:
            if n < 2:
                return 0
            return 1
        return 2
    i = 2
    for num in range(1, n):
        a = 6 * num - 1
        b = 6 * num + 1
        if a < n and judge(a) is None:
            i += 1
        if b < n and judge(b) is None:
            i += 1
    return i


def judge(n):
    for i in range(3, int(n ** 0.5 + 1), 2):
        a = n % i
        if a == 0:
            return i


@njit
def check_prime(num):
    tmp = int(np.sqrt(num)) + 1
    for i in range(2, tmp):
        if np.mod(num, i) == 0:
            return False
    return True


@njit
def prime_num(num):
    if num <= 2:
        return 0
    if num == 3:
        return 1
    i = 1
    up = num // 6 + 1
    res = 2
    while i <= up:
        h = 6 * i + 1
        low = 6 * i - 1
        res += check_prime(h) & (h < num)
        res += check_prime(low) & (low < num)
        i += 1
    return res


def countPrimes1(n: int) -> int:
    if n < 3:
        return 0
    else:
        output = [1] * n
        output[0], output[1] = 0, 0
        for i in range(2, int(n ** 0.5) + 1):
            if output[i] == 1:
                output[i * i:n:i] = [0] * len(output[i * i:n:i])
    return sum(output)


def countPrimes2(n):
    if n <= 2:
        return 0
    else:
        m = n // 2
        isPrimeOdd = [1] * m
        for i in range(1, int(math.sqrt(n)) // 2 + 1):
            if isPrimeOdd[i]:
                isPrimeOdd[2 * i * (i + 1):m:2 * i + 1] = [0] * ((m + i) // (2 * i + 1) - i)

        return sum(isPrimeOdd)


def countPrimes3(n):
    n -= 1
    if n < 2:  return 0

    r = int(n ** 0.5)
    V = [n // d for d in range(1, r + 1)]
    V += list(range(V[-1] - 1, 0, -1))
    S = {v: v - 1 for v in V}
    # 此时，可以认为S[v]中有数(2,3,4,...,v-1,v)，所以个数为v-1
    # S[v]中每个数乘d可以得到1到n中含因子d的所有合数
    # S[1]=0,S[2]=1,S[3]=2已经是最终结果
    # 在下面的每次循环中，逐步去掉S[v]中大于p且以p为因子，但不含比p小的因子的数
    # 即去掉S[v]中最小素数因子为p的合数

    for p in range(2, r + 1):
        # 小于n的所有合数的最小素数因子不可能大于r，所以只需要遍历2到r
        if S[p] == S[p - 1]:
            # p是合数，否则p是素数，S[p]至少比S[p-1]多出一个p来
            # 反过来，p是合数时，遍历到p时，已经遍历过p内的所有素数，S[p]中的所有合数必定已经筛掉，S[p] == S[p - 1]
            # 此时，S[key]中以p为因子的数，已经作为以p的最小素数因子为因子的数被筛掉，所以可以直接跳过
            continue
        # p是素数
        p2 = p * p
        sp_1 = S[p - 1]  # 1到p-1中的所有素数的个数
        for v in V:
            if v < p2:
                # v < p2 时，若为合数，素数因子小于p，已经遍历过了
                break
            S[v] -= S[v // p] - sp_1
            # 在做此计算前，S[v]和S[v//p]中，去掉了最小素数因子在1到p-1之间的合数
            # 所以S[v//p]中，去掉小于p的素数(S[p-1])，剩余数乘p即为S[v]中以p为最小素数因子的合数
    return S[n]


if __name__ == "__main__":
    x = 130808 * 2
    t1 = time.perf_counter()
    y = countPrimes3(130808)
    t2 = time.perf_counter()
    print(y, t2 - t1)
