class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        summ = 0
        
        def check(n):
            summ = 0

            if n in s: 
                return False

            s.add(n)

            while n:
                digit = n%10
                n = n//10
                summ+= digit**2

            if summ == 1:
                return True

            return check(summ)

        return check(n)
