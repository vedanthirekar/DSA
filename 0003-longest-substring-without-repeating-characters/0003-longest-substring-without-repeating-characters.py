class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """if we check s[r] in hmap, and if its value is 0, still it will return True.
        so instead i used this condition of hmap[s[r]]>0. 
        """

        l = 0
        n = len(s)
        maxx = 0
        hmap = Counter()
        for r in range(n):
            while hmap[s[r]] > 0:
                hmap[s[l]] -= 1
                l += 1
            # if s[r] not in hmap:
            hmap[s[r]] +=1
            maxx = max(maxx, r-l+1)

        return maxx