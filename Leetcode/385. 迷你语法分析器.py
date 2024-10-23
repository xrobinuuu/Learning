import json


def deserialize(s: str):
    j = json.loads(s)
    k = eval(s)
    print(j, k)


class NestedInteger:
    def __init__(self, s):
        self.s = s


if __name__ == "__main__":
    S = "[123,[456,[789]]]"

    deserialize(S)
