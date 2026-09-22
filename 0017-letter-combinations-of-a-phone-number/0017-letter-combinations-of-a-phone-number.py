class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        

        mapping = {"2":"abc","3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        curr = []
        def backtrack(curr, i):
            
            if i == len(digits):
                res.append("".join(curr))
                return

            for letter in mapping[digits[i]]:
                curr.append(letter)
                backtrack(curr, i+1)
                curr.pop() 

        backtrack(curr, 0)
        return res