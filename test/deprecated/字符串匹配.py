import re

import numpy as np
import pandas as pd

s = '-255      0    255,255,255;0.2   1  123,255,0;0.5 2 0,89,130;1 3 255,100,70'
# c = np.array([i.split(' ') for i in s.split(';')])
# a = c[:, 0]
# b = c[:, 1]
# d = c[:, 2]
# print(a)
# print(b)
# print(d)

df = pd.DataFrame(re.findall(r"(-?[0-9.]+)\s+(\d+)\s+([0-9,]+)", s), columns=['GRICODE', 'LEVEL', 'COLOR'])
df['GRICODE'] = df['GRICODE'].astype(float)
df['LEVEL'] = df['LEVEL'].astype(int)
print(df)
