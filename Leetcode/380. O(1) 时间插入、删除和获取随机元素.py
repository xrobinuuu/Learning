import random


class RandomizedSet:
    # def __init__(self):
    #     self.s = set()
    #
    # def insert(self, val: int) -> bool:
    #     if val in self.s:
    #         return False
    #     self.s.add(val)
    #     return True
    #
    # def remove(self, val: int) -> bool:
    #     if val in self.s:
    #         self.s.remove(val)
    #         return True
    #     return False
    #
    # def getRandom(self) -> int:
    #     return random.choice(list(self.s))

    def __init__(self):
        self.nums = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.indices[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        id = self.indices[val]
        self.nums[id] = self.nums[-1]
        self.indices[self.nums[id]] = id
        self.nums.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


if __name__ == "__main__":
    x = ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
    y = [[], [1], [2], [2], [], [1], [2], []]

    obj = RandomizedSet()
    print(obj.insert(1))
    print(obj.remove(2))
    print(obj.insert(2))
    print(obj.getRandom())
    print(obj.remove(1))
    print(obj.insert(2))
    print(obj.getRandom())
