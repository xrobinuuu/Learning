import re

import pandas as pd
import time

t1 = time.perf_counter()
s = "-10 255 255,255,255;0.1 0 255,255,255;5 1 202,243,177;10 2 153,211,132;25 3 116,181,92;50 4 127,182,243;100 5 0,47,212;250 6 211,84,239;5000 7 107,33,63"
rain = re.findall(r"(-?\d+\.?\d*)\s(\d+)\s(\d+,\d+,\d+)", s)
pd.DataFrame(rain)

t2 = time.perf_counter()

print(t2 - t1)
# print(data)
