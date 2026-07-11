class MinStack:

    def __init__(self):
        self.stack = []
        self.minn = [float("inf")]

    def push(self, value: int) -> None:
        self.stack.append(value)
        self.minn.append(min(self.minn[-1], value))

    def pop(self) -> None:
        self.stack.pop()
        self.minn.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minn[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()