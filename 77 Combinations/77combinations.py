class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = []
        combo = []

        def bt(start):
            if len(combo)==k:
                ans.append(combo[:])
                return
            
            for i in range(start,n+1):
                if i in combo:
                    continue
                
                combo.append(i)
                bt(i+1)
                combo.pop()

        bt(1)
        return ans

        