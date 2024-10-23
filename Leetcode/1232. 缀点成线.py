import numpy as np
from scipy.interpolate import interp1d


def checkStraightLine(coordinates):
    if len(coordinates) < 2:
        return True
    x = 0.000001
    j, z = coordinates.pop(0), coordinates.pop(0)
    m, n = j[1] - z[1], j[0] - z[0] + 0.0001
    k = m / n
    while coordinates:
        j = coordinates.pop(0)
        m, n = j[1] - z[1], j[0] - z[0] + 0.0001
        k1 = m / n
        if k != k1:
            return False
        z = j

    return True


def i_l(coordinates):
    c = np.array(coordinates)
    f = interp1d(c[[0, 1], 0], c[[0, 1], 1], fill_value='extrapolate')
    r = f(c[2:, 0])
    return np.all(c[2:, 1] == r)


if __name__ == '__main__':
    Coordinates = [[0, 0], [0, 1], [0, -1]]
    y = checkStraightLine(Coordinates)
    print(y)
    # x = i_l(Coordinates)
    # print(x)
