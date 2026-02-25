class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, sol = [], []

        def bt(openn, close):
            if len(sol) == 2*n:
                ans.append("".join(sol))
                return

            if openn < n:
                sol.append("(")
                bt(openn+1, close)
                sol.pop()

            if openn>close:
                sol.append(")")
                bt(openn,close+1)
                sol.pop()

        bt(0,0)
        return ans