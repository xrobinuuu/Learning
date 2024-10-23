import threading
import time
from concurrent.futures import ThreadPoolExecutor
import threading


def juest(n):
    global ls
    if n == 40:
        time.sleep(1)
        ls.append(n)
    else:
        time.sleep(2)


ls = []
t_1 = time.perf_counter()
pool = ThreadPoolExecutor(max_workers=24)
for i in range(100):
    pool.submit(juest, i)
    if ls:
        t_2 = time.perf_counter()
        print(ls[0])
        print(t_2 - t_1)
        break