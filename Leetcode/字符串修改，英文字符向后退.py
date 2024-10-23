
import time


def trans(st, num):
    asc_id = ord(st)
    if 96 < asc_id < 123:
        asc_chr = chr(96 + (asc_id + int(num) - 96) % 26)
    else:
        asc_chr = chr(64 + (asc_id + int(num) - 64) % 26)
    return asc_chr


t1 = time.perf_counter()

char = "a" * 10000
nu = 1
tmp_dict = dict()
res = str()
for s in char:
    if s.isalpha():
        if s not in tmp_dict:
            trs = trans(s, nu)
            tmp_dict.update({s: trs})
        res += tmp_dict[s]

    else:
        res += s
t2 = time.perf_counter()
print(char)
print(res)
print(t2 - t1)
