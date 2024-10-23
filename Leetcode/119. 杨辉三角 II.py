def getRow(num):
    ls = [[1], ]
    for i in range(1, num + 1):
        ls.append([])
        for z in range(i + 1):
            if z == 0 or z == i:
                ls[i].append(1)
            else:
                ls[i].append(ls[i - 1][z - 1] + ls[i - 1][z])
    return ls[num]


if __name__ == "__main__":
    nu = 3
    y = getRow(nu)
    print(y)
