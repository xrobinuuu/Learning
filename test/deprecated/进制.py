import copy
import math
import random
import numpy as np


def o_2_7(n, t_8, t_7):
    v = copy.deepcopy(n)
    vst = dict(zip(range(7), [0] * 7))
    vst2 = dict(zip(range(8), [0] * 8))
    for j in range(n):
        s_o = "".join([str(random.randint(0, 7)) for i in range(t_8)])
        n_s_o = int(s_o, 8)
        if n_s_o >= pow(7, t_7):
            v -= 1
            continue
        r = n_s_o % 7
        r2 = n_s_o % 8
        vst2.update({r2: vst2[r2] + 1})
        vst.update({r: vst[r] + 1})
    res2 = np.array(list(vst2.values())) / v
    res = np.array(list(vst.values())) / v
    print(np.mean(res), np.std(res), res)
    print(np.mean(res2), np.std(res2), res2)


def best_diff(n):
    n_1 = 1
    n_2 = int(n_1 * math.log(8, 7))
    t_1 = (pow(8, n_1) - pow(7, n_2)) / pow(8, n_1)
    for i in range(n):
        i2 = int(i * math.log(8, 7))
        if i2 > 0:
            t_2 = (pow(8, i) - pow(7, i2)) / pow(8, i)
            if t_2 < t_1:
                t_1 = t_2
                n_1 = i
                n_2 = i2
    return n_1, n_2


n_8, n_7 = best_diff(10000)
print(n_8, n_7)

o_2_7(10000, n_8, n_7)