import numpy as np
from scipy.interpolate import Rbf, griddata
from scipy.stats import pearsonr


def interp_gg_linear(d, z):
    n = len(d) - 1
    x = int(z[0][0])
    y = int(z[0][1])
    x1 = min(x + 1, n)
    y1 = min(y + 1, n)
    dx = z[0][0] - x
    dy = z[0][1] - y
    c00 = (1 - dx) * (1 - dy)
    c10 = dx * (1 - dy)
    c11 = dx * dy
    c01 = (1 - dx) * dy
    d = c00 * d[x, y] + c10 * d[x1, y] + c11 * d[x1, y1] + c01 * d[x, y1]
    return d


def gg(d, z):
    lon = np.arange(d.shape[1])
    lat = np.arange(d.shape[0])
    lon1, lat1 = np.meshgrid(lon, lat)
    f = Rbf(lat1, lon1, d, function='linear')
    return f(z[:, 0], z[:, 1])


def gg2(d, z):
    lon = np.arange(d.shape[1])
    lat = np.arange(d.shape[0])
    lon1, lat1 = np.meshgrid(lon, lat)
    points = np.c_[lat1.flatten(), lon1.flatten()]
    return griddata(points, d[points[:, 0], points[:, 1]], z)


if __name__ == '__main__':
    m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    lx = 2 * np.random.random((10, ))
    ly = 2 * np.random.random((10, ))
    Z = np.c_[lx, ly]
    v = interp_gg_linear(m, Z)
    print(v)
    v1 = gg(m, Z)
    print(v1)
    v2 = gg2(m, Z)
    print(v2)
    r1 = np.corrcoef(v1, v2)[0, 1]
    print(r1)
    r2 = pearsonr(v1, v2)[0]
    print(r2)