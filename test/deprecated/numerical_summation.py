import time
from multiprocessing.pool import Pool
from multiprocessing import Manager



def timer(func):
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = await func(*args, **kwargs)
        end = time.perf_counter()
        print(end - start, result)
        return result

    return wrapper


class Arithmetic:

    def __init__(self):
        manager = Manager()
        self.sum_num = manager.Value('i', 0)

    def arithmetic_sequence(self, begin, end, step: int = 1):
        n = (end - begin) // step + 1
        self.sum_num.value += n * (2 * begin + (n - 1) * step) // 2

    def multi_arithmetic(self, begin: int, end: int, chunk=10000):
        with Pool(10) as pool:
            for sub_begin in range(begin, end, chunk):
                sub_end = end if sub_begin + chunk - 1 > end else sub_begin + chunk - 1
                pool.apply(func=self.arithmetic_sequence, args=(sub_begin, sub_end))
            pool.close()
            pool.join()
        print(self.sum_num)


if __name__ == '__main__':
    Arithmetic().multi_arithmetic(1, 100000)
