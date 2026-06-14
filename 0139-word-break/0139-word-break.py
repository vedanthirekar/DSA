class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        memo = {}
        def dfs(i, word):
            if i == n:
                if word == s:
                    return True
            
            if word !=s [:i]:
                return False

            if (i,word) in memo:
                return memo[(i,word)]

            for words in wordDict:
                if dfs(i+len(words), word+words):
                    memo[(i,word)] = True
                    return memo[(i,word)]
            memo[(i,word)] = False
            return memo[(i,word)]

        return dfs(0, "" )
        
