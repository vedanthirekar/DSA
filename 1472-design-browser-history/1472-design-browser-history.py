class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.curr_step = 1

    def visit(self, url: str) -> None:
        if self.curr_step < len(self.stack):
            for _ in range(len(self.stack)-self.curr_step):
                self.stack.pop()
        
        
        self.stack.append(url)
        self.curr_step = len(self.stack)

    def back(self, steps: int) -> str:
        if steps>=self.curr_step-1:
            self.curr_step = 1
            return self.stack[0]


        self.curr_step -= steps
        return self.stack[self.curr_step-1]

    def forward(self, steps: int) -> str:
        if len(self.stack)-self.curr_step<= steps:
            self.curr_step = len(self.stack)
            return self.stack[-1]

        self.curr_step += steps
        return self.stack[self.curr_step-1]      


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)