class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        """we start at the end and move inwards while checking for conditoisn of similarity"""
        
        n = len(colors)
        l = 0
        r = n-1
        if n==2:
            return 1 if colors[0]!=colors[1] else 0

        while colors[l] == colors[r]:
            r-=1

        a = r-l

        l= 0
        r = n-1
        while colors[l] == colors[r]:
            l+=1
        b = r-l

        return max(a,b) 