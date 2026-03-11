class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        curr = 2

        if n ==1:
            return 1

        for i in range(n-2):
            prev, curr = curr, prev+curr

        return curr