class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = 0 
        r = len(s)-1

        while l<=r:
            while l<r and not s[l].isalnum():
                l+=1
            while l< r and not s[r].isalnum():
                r-=1

            print("left", l, s[l])
            print("right", r, s[r])
            if s[r].lower() != s[l].lower():
                print ("False")
                return False

            l+=1
            r-=1

        return True
            