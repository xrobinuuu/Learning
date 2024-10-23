import os
import time
from multiprocessing import Process, Pool, Queue, Manager


def two_sum(nums, target):
    dic = dict()
    for i, n in enumerate(nums):
        if target - n in dic:
            return [i, dic[target - n]]
        dic.update({n: i})


def two_sum_mp(ls_num, ls, all_num):
    for num in ls_num:
        res = all_num - num
        if res in ls:
            return [len(ls), ls[res]]
        ls.update({num: len(ls)})


def mp_num(ls, num):
    did = os.cpu_count()
    pool = Pool(processes=5)
    step = len(ls) // did + 1
    p_ls = list()
    for i in range(1, did):
        dic = dict(zip(ls[:i*step], range(i*step)))
        p = pool.apply_async(func=two_sum_mp, args=(ls[i*step: (i+1)*step], dic, num))
        p_ls.append(p)
    for tmp in p_ls:
        print(tmp)
        res = tmp.get()
        print(res)
        if res:
            return res


if __name__ == "__main__":
    li = list(range(5 * (10 ** 3)))
    result = li[-1] + li[-2]
    # with Manager() as manager:
    #     dic = manager.dict()
    #     res = manager.list()
    #     pool = Pool(16)
    #     for i in range(16):
    #         pool.apply_async(func=two_sum, args=(li, 5 * (10 ** 5), dic, res))
    #
    #     pool.close()
    #     pool.join()
    #     t2 = time.perf_counter()
    #     print(t2 - t1)
    #     print(res)
    t1 = time.perf_counter()
    x = mp_num(li, result)
    # x = two_sum(li, result)
    t2 = time.perf_counter()
    print(x)
    print(t2 - t1)