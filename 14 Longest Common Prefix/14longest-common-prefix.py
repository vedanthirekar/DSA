class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        check = strs[0]
        ans = float("inf")
        for i in strs:
            # k = 0
            j = 0
            for k in range(min(len(check), len(i))):
                if i[k] == check[k]:
                    j += 1
                    
                else:
                    break

            ans = min(ans, j)

        return check[:ans]