class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapper = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        n = len(digits)
        ans = []
        res = [] 

        def dfs(ans, i, curr_len):
            if curr_len == n:
                res.append("".join(ans[:]))
                return

            for char in mapper[digits[i]]:
                ans.append(char)
                dfs(ans, i+1, curr_len+1)
                ans.pop()
            

        dfs([],0, 0)
        return res

        
