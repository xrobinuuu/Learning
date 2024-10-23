import collections


def get_dict_final(n, dic):
    for tmp in n:
        if n not in dic:
            return n
    return get_dict_final(dic.pop(n), dic)


# def fix_path(n, connections):
#     a2b, b2a = collections.defaultdict(set), collections.defaultdict(set)
#     for i, j in connections:
#         a2b[i].add(j)
#         b2a[j].add(i)
#     s = [0]
#     seen = set(s)
#     cnt = 0
#     while s:
#         city = s.pop()
#         for nxt in b2a[city] | a2b[city]:
#             if nxt not in seen:
#                 cnt += nxt in a2b[city]
#                 seen.add(nxt)
#                 s.append(nxt)
#     return cnt


def fix_path(n, connections):
    path_1 = dict()
    path_2 = dict()
    for path in connections:
        tmp_ls_1 = path_1.get(path[0], [])
        tmp_ls_2 = path_2.get(path[1], [])
        tmp_ls_1.append(path[1])
        tmp_ls_2.append(path[0])
        path_1.update({path[0]: tmp_ls_1})
        path_2.update({path[1]: tmp_ls_2})
    print(path_1)
    print(path_2)
    path_ls = [0]
    count = 0
    visited = set()
    while path_ls:
        p = path_ls.pop()
        # if p in visited: continue
        if p in path_2.keys():
            for i in path_2[p]:
                if i not in visited:
                    path_ls.append(i)
                    visited.add(p)
        if p in path_1.keys():
            for i in path_1[p]:
                if i not in visited:
                    path_ls.append(i)
                    visited.add(p)
                    count += 1
    return count


if __name__ == "__main__":
    conn = [[1, 0], [2, 1], [3, 0], [2, 4], [3, 5], [4, 6], [7, 3], [6, 8], [9, 0], [4, 10], [9, 11], [8, 12], [13, 12],
            [7, 14]]
    num = 15
    x = fix_path(num, conn)
    print(x)
