class MinStack:

    def __init__(self):
        self.ls = []

    def push(self, val: int) -> None:
        self.ls.append(val)

    def pop(self) -> None:
        del self.ls[-1]

    def top(self) -> int:
        return self.ls[-1]

    def getMin(self) -> int:
        return min(self.ls)


if __name__ == "__main__":
    minStack = MinStack()
    print(minStack.push(-2))
    print(minStack.push(0))
    print(minStack.push(-3))
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.top())
    print(minStack.getMin())
