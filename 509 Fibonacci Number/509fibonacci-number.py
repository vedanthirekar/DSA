class Solution:
    def fib(self, n: int) -> int:
        curr = 1
        prev = 0
        if n == 0:
            return 0
            
        for i in range(1,n):
            curr ,prev = curr+prev, curr
        
        return curr