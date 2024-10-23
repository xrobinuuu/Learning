def threeConsecutiveOdds(arr: list[int]) -> bool:
    ind = 0
    for i, v in enumerate(arr, 1):

        if v % 2:
            print(i, ind)
            if i - ind >= 3:
                return True
        else:
            ind = i
    return False


if __name__ == '__main__':
    Arr = [1,2,1,1,1]
    y = threeConsecutiveOdds(Arr)
    print(y)