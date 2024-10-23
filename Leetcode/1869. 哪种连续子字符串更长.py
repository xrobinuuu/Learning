import gc
import multiprocessing
import random
import re
import time
import psutil
import os


def checkZeroOnes(s: str) -> bool:
    t1 = time.perf_counter()
    x = list(map(lambda x: len(x), re.findall(r"(0+)", s)))
    y = list(map(lambda x: len(x), re.findall(r"(1+)", s)))
    x, y = max(x) if x else 0, max(y) if y else 0
    t2 = time.perf_counter()
    print(f'xrb: {t2 - t1}')
    print(u'xrb 当前进程的内存使用：%.4f MB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024))
    return y > x


def lik(s):
    t1 = time.perf_counter()
    x1 = len(max(s.split('0')))
    y1 = len(max(s.split('1')))
    t2 = time.perf_counter()
    print(f'lk: {t2 - t1}')
    print(u'lik 当前进程的内存使用：%.4f MB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024))
    return x1 > y1


def find_str_max(s):
    t1 = time.perf_counter()
    max_dict = {'0': 0, '1': 1}
    i = j = 0
    le = len(s)
    while j < le:
        j += 1
        if j == le or s[i] != s[j]:
            tmp = j - i
            if tmp > max_dict.get(s[i]):
                max_dict.update({s[i]: tmp})
            i = j
    gc.collect()
    t2 = time.perf_counter()
    print(f'lsk: {t2 - t1}')
    print(u'lsk 当前进程的内存使用：%.4f MB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024))
    return max_dict['1'] > max_dict['0']


if __name__ == "__main__":
    sam = '01'
    s1 = ''.join(['0'*i + '1'*i for i in range(10000)])
    # s1 = ''.join(random.choices(sam, k=1000000))
    pool = multiprocessing.Pool(processes=3)
    pool.apply_async(func=checkZeroOnes, args=(s1, ))
    pool.apply_async(func=find_str_max, args=(s1, ))
    pool.apply_async(func=lik, args=(s1, ))
    pool.close()
    pool.join()