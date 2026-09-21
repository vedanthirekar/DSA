class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        max_amount = 0
        l = 0
        r = len(height)-1

        while l<r:
            curr_amount = (r-l) * min(height[r], height[l])

            max_amount = max(max_amount, curr_amount)

            if height[r]<height[l]:
                r-=1
            else:
                l+=1

        return max_amount

