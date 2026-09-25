class MinStack:

    def __init__(self):
        self.stack = []
        self.min_till_now = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minn = self.min_till_now[-1] if self.min_till_now else float("inf")
        self.min_till_now.append(min(val,minn))

    def pop(self) -> None:
        self.min_till_now.pop()
        return self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_till_now[-1]
