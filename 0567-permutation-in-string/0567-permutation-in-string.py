class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # return Counter(s1)<Counter(s2)
        n1 = len(s1)
        n2 = len(s2)
        if n2<n1:
            return False

        c1 = Counter(s1)
        c2 = Counter(s2[:n1])

        l = 0
        r = n1-1
        while r<n2:
            if c1 == c2:
                return True
            c2[s2[l]] -=1
            l+=1
            r+=1
            if r<=n2-1:
                c2[s2[r]]+=1

        return False