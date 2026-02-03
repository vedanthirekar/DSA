class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for t in tokens:
            if t == "+":
                a = stk.pop()
                b = stk.pop()
                c = a + b
                stk.append(c)
            elif t == "*":
                a = stk.pop()
                b = stk.pop()
                stk.append(a*b)
                # print(stk)
            elif t == "-":
                a = stk.pop()
                b = stk.pop()
                stk.append(b-a)
            elif t == "/":
                a = stk.pop()
                b = stk.pop()
                stk.append(int(b/a))
            else:
                stk.append(int(t))
                # print(stk)

        return stk[0]
        