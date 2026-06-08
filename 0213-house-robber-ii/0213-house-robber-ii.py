class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        nums1 = nums[:n-1]
        nums2 = nums[1:]


        def max_amt(s_nums):
            # if not s_nums:
            #     return 0
            s_n = n-1
            if s_n<3:
                return max(s_nums)
            prev = s_nums[0]
            curr = max(prev,s_nums[1])


            for i in range(2,s_n):
                temp = curr
                curr = max(curr, prev+s_nums[i])
                prev = temp
                

            return curr 

        if n ==1:
            return nums[0]
        a1 = max_amt(nums1)
        a2 = max_amt(nums2)

        return max(a1,a2)
