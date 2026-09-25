class MinStack:

    # def __init__(self):
    #     self.stack = []
    #     self.min_till_now = []

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     minn = self.min_till_now[-1] if self.min_till_now else float("inf")
    #     self.min_till_now.append(min(val,minn))

    # def pop(self) -> None:
    #     self.min_till_now.pop()
    #     return self.stack.pop()


    # def top(self) -> int:
    #     return self.stack[-1]

    # def getMin(self) -> int:
    #     return self.min_till_now[-1]

    def __init__(self):
        self.stack = []
        self.min = float("inf")

    def push(self, val):
        if not self.stack:
            self.stack.append(0)
            self.min = val
            return
        
        self.stack.append(val-self.min)
        if val<self.min:
            self.min = val

    def pop(self):
        if not self.stack:
            return 
        
        pop_val = self.stack.pop()
        if pop_val>0:
            return pop_val+self.min

        else:
            return_val = self.min
            self.min = self.min - pop_val
            return return_val

    def top(self):
        if not self.stack:
            return
        if self.stack[-1]<0:
            return self.min
            
        return self.min+self.stack[-1]

    def getMin(self):
        return self.min

