class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minn = float("inf")
        n1 = len(s)
        n2 = len(t)
        out_r = 0
        out_l = 0
        r = n2-1
        l = 0

        c1 = Counter(s[:n2])
        c2 = Counter(t)
        while r<n1:
            while c2<=c1:
                if r-l+1< minn:
                    out_r = r
                    out_l = l
                    minn = min(minn, r-l+1)
                c1[s[l]] -=1
                l+=1
            
            r+=1
            if r<n1:
                c1[s[r]]+=1
        
        return "" if minn == float("inf") else s[out_l:out_r+1] 

        