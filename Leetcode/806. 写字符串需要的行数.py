import string


def num_line(w: list, s: str):
    if not s:
        return [1, 0]
    tem = dict(zip(string.ascii_lowercase, w))[s[-1]]
    tem_ls = num_line(w, s[:-1])
    total = tem + tem_ls[1]
    return [tem_ls[0] + 1, tem] if total > 100 else [tem_ls[0], total]


if __name__ == "__main__":
    # widths = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    # S = "bbbcccdddaaa"

    widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    S = "abcdefghijklmnopqrstuvwxyz"

    x = num_line(widths, S)
    print(x)
