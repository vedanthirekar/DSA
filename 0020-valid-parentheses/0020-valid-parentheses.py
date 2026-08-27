class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")":"(", "]": "[", "}":"{"}
        stk = []
        for bracket in s:
            if bracket in mapping and stk:
                b = stk.pop()
                if mapping[bracket] != b:
                    return False
            else:
                stk.append(bracket)
        
        return True if not stk else False
