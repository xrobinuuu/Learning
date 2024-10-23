import numpy as np


def pccs(x, y):
    n = len(x)
    sumx = np.sum(x).astype(float)
    sumy = np.sum(y).astype(float)
    xy = np.sum(x * y).astype(float)
    x2 = np.sum(x * x).astype(float)
    y2 = np.sum(y * y).astype(float)
    num = xy - sumx * sumy / n
    den = np.sqrt((x2 - pow(sumx, 2) / n) * (y2 - pow(sumy, 2) / n))
    return num / den


m = np.array([11, 2, 323, 445, 5])
n = np.array([1, 2, 3245, 4435, 5])

pccs1 = pccs(m, n)
pccs2 = np.corrcoef(m, n)
print(pccs1)
print(pccs2)

