# c = str(secret)
# print(c)
# print(bytes(secret))


def str_to_byte(ms, word_byte=""):
    for s in ms:
        w = str(bin(ord(s)))[2:]
        word_byte += "0" * (16 - len(w)) + w
    return word_byte


def byte_to_str(bs, word=""):
    for b in range(1, int(len(bs) / 16) + 1):
        word += chr(int(bs[(b - 1) * 16: b * 16], 2))
    return word


if __name__ == "__main__":
    my_str = "你晚上吃什么，食堂吗。"
    x = str_to_byte(my_str)
    print(x)

    secret = '011011001010000110010100101100010110011000101111100011111101100101101000001101110111011010000100'
    y = byte_to_str(secret)
    print(y)
