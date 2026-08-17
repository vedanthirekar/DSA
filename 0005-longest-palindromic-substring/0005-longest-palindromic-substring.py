class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        longest = 0
        for i in range(n):
            curr_longest = 1
            l = i-1
            r = i+1
            while l>=0 and r<n and s[l] == s[r]:
                curr_longest += 2 
                l-=1 
                r+=1
            if curr_longest> longest:
                res = s[l+1:r]
                longest = curr_longest

        for i in range(n-1):
            if s[i] == s[i+1]:
                curr_longest = 2
                l = i-1
                r = i+2
                while l>=0 and r<n and s[l] == s[r]:
                    curr_longest += 2 
                    l-=1 
                    r+=1
            if curr_longest> longest:
                res = s[l+1:r]
                longest = curr_longest

        return res
