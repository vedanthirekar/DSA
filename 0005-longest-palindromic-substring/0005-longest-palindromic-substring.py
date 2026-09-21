class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest = 0
        res = ""

        for i in range(len(s)):
            l = i-1
            r = i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                l -=1
                r +=1

            if r-l-1>longest:
                longest = r-l-1
                res = s[l+1: r]


            l = i
            r = i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                l -=1
                r +=1

            if r-l-1>longest:
                longest = r-l-1
                res = s[l+1: r]


        return res