import string


# def find_words(code):
#     def ms_to_str(le, co, e, s, ms_word="", word=""):
#         i = 1
#         while i < 5:
#             a, b = co[: i], co[i:]
#             i += 1
#             if a not in le: continue
#             if ms_word + a == ms_word + a + b:
#                 return s.append(word + le[a])
#             ms_to_str(le, b, 1, s, ms_word + a, word + le[a])
#     msc = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
#            ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
#     ls = list()
#     end = 1
#     letter = dict(zip(msc, string.ascii_lowercase))
#     while end < 5:
#         ms_to_str(letter, code, end, ls)
#         end += 1
#     return ls


def find_words(code):
    msc = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
           ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    ls = list()
    letter = dict(zip(msc, string.ascii_lowercase))
    code = "".join([code, "/", "/"]) if "/" not in code else code
    co, ms_word, word = code.split("/")
    i = 1
    while i < 5:
        a, b = co[: i], co[i:]
        i += 1
        if a not in letter: continue
        if ms_word + a == ms_word + a + b:
            ls.append(word + letter[a])
        ls = ls + find_words("/".join([b, ms_word + a, word + letter[a]]))
    return ls


def mos2words_1(mos):
    mos_dic = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h',
               '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p',
               '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
               '-.--': 'y', '--..': 'z'}
    res = dict()
    for i in range(1, 5):
        if mos[:i] in mos_dic:
            res[mos_dic[mos[:i]]] = mos[i:]
    return res


def mos2words_2(mos_dict):
    res = dict()
    for k, v in mos_dict.items():
        if not v:
            res[k] = v
        tmp = mos2words_1(v)
        for i, j in tmp.items():
            res[k + i] = j
    return res


def mos2words_3(mos):
    mos_d = mos2words_1(mos)
    result = ''.join(list(mos_d.values()))
    while result:
        mos_d = mos2words_2(mos_d)
        result = ''.join(list(mos_d.values()))
    return list(mos_d.keys())


if __name__ == "__main__":
    # code = "--...--."  # words = ["gin", "zen", "gig", "msg"]
    # z = find_words(letter, code, [])
    # print(z)

    code_x = "--...--."  # words = ["gin", "zen", "gig", "msg"]
    code_y = '--...-.'

    z = mos2words_3(code_x)
    k = mos2words_3(code_y)
    z.extend(k)
    x = find_words(code_x)
    y = find_words(code_y)
    x.extend(y)
    x = list(set(x))
    z.sort()
    x.sort()
    print(z == x)
    # print(len(set(x)))
    # lst = ["gin", "zen", "gig", "msg"]
    # for n in lst:
    #     print(n in x)