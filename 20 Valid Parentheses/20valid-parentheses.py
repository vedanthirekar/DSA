class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"}":"{",")":"(","]":"["}
        li = []
        # if s[0] not in hashmap.values():
        #     return False
        for i in s:
            if i in hashmap.values():
                li.append(i)
            else:
                if not li:
                    return False
                a = li.pop()
                if hashmap[i] != a:
                    return False
        
        return False if li else True