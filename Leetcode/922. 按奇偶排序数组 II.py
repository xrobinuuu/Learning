def sortArrayByParityII(arr: list[int]):
    def tran(num):
        return (1, num) if num % 2 else (0, num)

    arr.sort(key=tran)
    ls = []
    ind = 1
    while arr:
        ls.append(arr.pop(ind % 2 - 1))
        ind += 1
    return ls


if __name__ == "__main__":
    Nums = [4, 2, 5, 7]
    x = sortArrayByParityII(Nums)
    print(x)


