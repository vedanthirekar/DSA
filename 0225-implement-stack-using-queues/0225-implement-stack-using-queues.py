from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        # self.q2 = deque()
        self.size = 0

    def push(self, x: int) -> None:
        # for i in range(self.size-1):
        #     self.q1.append(self.q1.popleft())

        self.q1.append(x)
        self.size += 1

        for i in range(self.size-1):
            self.q1.append(self.q1.popleft())


    def pop(self) -> int:
        res = self.q1.popleft()
        self.size -=1
        return res

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return self.size == 0


    # def __init__(self):
    #     self.q1 = deque()
    #     self.q2 = deque()
    #     self.size = 0

    # def push(self, x: int) -> None:
    #     self.q1.append(x)
    #     self.size += 1

    # def pop(self) -> int:
    #     for i in range(self.size -1):
    #         self.q2.append(self.q1.popleft())
    #     res = self.q1.popleft()
    #     self.q1 = self.q2
    #     self.q2 = deque()
    #     self.size -=1
    #     return res

    # def top(self) -> int:
    #     for i in range(self.size -1):
    #         self.q2.append(self.q1.popleft())
    #     res = self.q1.popleft()
    #     self.q2.append(res)
    #     self.q1 = self.q2
    #     self.q2 = deque()
    #     return res

    # def empty(self) -> bool:
    #     return True if self.size==0 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()