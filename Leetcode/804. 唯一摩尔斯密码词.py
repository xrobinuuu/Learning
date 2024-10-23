import string


def ms_code(m, to_ms):
    # dic = dict()
    # fig = set()
    # for i in range(97, 123):
    #     dic[chr(i)] = m[i - 97]

    dic = dict(zip(string.ascii_lowercase, m))
    print(dic)
    return len(set([''.join(map(lambda a: dic[a], list(word))) for word in to_ms]))


if __name__ == "__main__":
    ms = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
          ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    # words = ["gin", "zen", "gig", "msg"]
    words = ["a"]
    code = ms_code(ms, words)
    print(code)
