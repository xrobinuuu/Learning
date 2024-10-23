import time
import asyncio


def timer(func):
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = await func(*args, **kwargs)
        end = time.perf_counter()
        print(end - start)
        return result

    return wrapper


class Arithmetic:

    def __init__(self):
        self.total = 0
        self.part = 0

    async def arithmetic_sequence(self, begin, end, step: int = 1):
        n = (end - begin) // step + 1
        self.total += n * (2 * begin + (n - 1) * step) // 2
        await asyncio.sleep(1)
        print(self.part)
        self.part += 1

    @timer
    async def multi_arithmetic(self, begin: int, end: int, chunk=1000000):
        tasks = []
        for sub_begin in range(begin, end, chunk):
            sub_end = end if sub_begin + chunk - 1 > end else sub_begin + chunk - 1
            tasks.append(self.arithmetic_sequence(sub_begin, sub_end))
        await asyncio.gather(*tasks)
        print(self.total)


if __name__ == '__main__':
    asyncio.run(Arithmetic().multi_arithmetic(1, 10000000))
