class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        counter1 = Counter(s1)
        l1 = len(s1)
        l2 = len(s2)
        for i in range(l2-l1+1):
            counter2 = Counter(s2[i:i+l1])

            if counter1 == counter2:
                return True

        return False