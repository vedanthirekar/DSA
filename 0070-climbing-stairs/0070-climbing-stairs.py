class Solution:
    def climbStairs(self, n: int) -> int:
        """at each step we can either take 1 step or 2 steps. we can try to form a tree with this.
        As we reach at one end, we return 1 for that path/way
        """
        memo = {}
        def dfs(steps):
            if steps in memo:
                return memo[steps]
            if steps+1 == n:
                return 1
            if steps+2 ==n:
                return 2
            
            memo[steps] = dfs(steps+1) + dfs(steps+2)
            return memo[steps]


        return dfs(0)