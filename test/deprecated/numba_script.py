import asyncio
import time

ls = [i for i in range(70000000)]


async def number_sum(l):
    asyncio.sleep(1)
    total = 0
    for i in l:
        total += i
    asyncio.sleep(2)
    return total


async def number_dot(l):
    asyncio.sleep(1)
    total = 0
    for i in l:
        total *= i
    return total


if __name__ == '__main__':
    t1 = time.perf_counter()
    result = number_sum(ls)
    result += number_dot(ls)
    t2 = time.perf_counter()
    print(t2 - t1)
    print(result)
