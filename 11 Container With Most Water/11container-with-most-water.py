class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        n = len(height)
        r = n-1
        curr = 0
        max_curr = 0
        while l<r:
            curr = min(height[r], height[l])*(r-l)
            if height[r]>height[l]:
                l += 1
            else:
                r -=1            
            max_curr = max(curr, max_curr)
        return max_curr

        