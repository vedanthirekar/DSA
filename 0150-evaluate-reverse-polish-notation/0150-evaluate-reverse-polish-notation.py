class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stk = []
        n = len(tokens)
        operators = ["+", "-", "*", "/"]
        for t in tokens:
            if t in operators:
                a = stk.pop()
                b = stk.pop()
                operator = t
                val = 0
                if operator == "+":
                    val = int(a)+int(b)
                elif operator == "-":
                    val = int(b)-int(a)
                elif operator == "*":
                    val = int(a)*int(b)
                elif operator == "/":
                    val = math.trunc(int(b)/int(a))

                stk.append(str(val))
            else:
                stk.append(t)

        return int(stk[-1])