
def main(n):
    dic = {1: 1, 2: 2}
    for i in range(3, n + 1):
        dic.update({i: dic.get(i - 1) + dic.get(i - 2)})
    return dic.get(n)


def stage_function(n):
    visited = {}

    if n == 1:
        return 1
    if n == 2:
        return 2

    return stage_function(n-1) + stage_function(n-2)


if __name__ == "__main__":
    # x = stage_solution(5)
    # print(x)
    x = main(100)
    print(x)