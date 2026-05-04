class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        n = len(height)
        r = n-1
        maxx = 0
        while l<r:
            area = (r-l)*min(height[l],height[r])
            maxx = max(maxx,area)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return maxx