class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # def isPal(s):
        #     #O(n) time and space
        #     # return s[::-1] 
            
        #     #O(n) time and O(1) space
        #     l = 0
        #     r = len(s)-1
        #     while l<r:
        #         if s[l] != s[r]:
        #             return False
        #         l+=1
        #         r-=1
        #     return True

        res = 0
        n = len(s)

        for i in range(n):
            res +=1
            l = r = i
            while l>0 and r<n-1 and s[l-1] == s[r+1]:
                res +=1
                l -=1
                r +=1
            
        for i in range(n-1):
            if s[i] == s[i+1]:
                res+=1
                l = i
                r = i+1
                while l>0 and r<n-1 and s[l-1] == s[r+1]:
                    res +=1
                    l -=1
                    r +=1

        return res




