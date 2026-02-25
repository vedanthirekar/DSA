class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        a = []
        sol = []

        if digits == "":
            return []

        letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def bt(i = 0):

            if i ==len(digits):
                sol.append("".join(a))
                return 
        
            for letter in letter_map[digits[i]]:
                a.append(letter)
                bt(i+1)
                a.pop()

        bt(0)
        return sol
