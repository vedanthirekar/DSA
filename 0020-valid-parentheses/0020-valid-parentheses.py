class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {")":"(", "}":"{", "]":"["}

        stk = []
        # stk.append(s[0])
        n = len(s)
        for i in s:
            if i in pairs.values():
                stk.append(i)
            elif stk and pairs[i] == stk[-1]:
                stk.pop()
            else:
                return False
        
        return not stk