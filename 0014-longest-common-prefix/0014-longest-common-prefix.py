class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(w) for w in strs)
        n = len(strs)
        res = ""
        for i in range(min_len):
            flag = True
            for word in strs:
                if word[i] !=strs[0][i]:
                    flag = False
                    break
            if flag:
                res += strs[0][i]
            else:
                break

        return res