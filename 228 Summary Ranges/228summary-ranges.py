class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        strr = ""
        l = []
        i = 0
        while i<len(nums):
            strr = ""
            if i == len(nums)-1:
                l.append(str(nums[i]))
            
            elif nums[i]+1 != nums[i+1]:
                l.append(str(nums[i]))
                # i += 1
            else:
                strr = str(nums[i])
                while i+ 1<len(nums) and nums[i]+1 == nums[i+1]:
                    i += 1
                strr = strr + "->" + str(nums[i])
                l.append(strr)
                # i += 1
            i += 1
        return l


            