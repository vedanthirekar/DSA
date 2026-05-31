class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        max_f = 0
        n = len(s)
        hashmap = Counter()
        maxx = 0
        for r in range(n):
            hashmap[s[r]] += 1
            max_f = max(hashmap.values())
            while r-l+1-max_f>k:
                hashmap[s[l]] -= 1
                l+=1

            maxx = max(maxx, r-l+1)

        return maxx