class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 = {"I": 1, "V":5, "X":10, "L":50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        i = len(s)-1
        while i>=0:
            if (i-1) >= 0 and dict1[s[i-1]]<dict1[s[i]]:
                sum += dict1[s[i]]-dict1[s[i-1]]
                i -=2
            else:
                sum += dict1[s[i]]
                i -=1
        
        return sum
