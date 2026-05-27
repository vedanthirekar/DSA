# class Solution:
#     def search(self, nums: List[int], target: int) -> int:

#             l = 0
#             h = len(nums)-1
#             m = 0
#             while l <h:
#                 m = l+ (h-l)//2
#                 if nums[m]<nums[h]:
#                     h = m
#                 else:
#                     l = m+1
#             # print (m)


#             h = len(nums)-1
#             l = 0
#             if target>=nums[m] and target<=nums[h]:
#                 l = m
#             else:
#                 h = m-1

#             while l<=h:
#                 m = l+(h-l)//2
#                 if nums[m]== target:
#                     return m
#                 elif nums[m]>target:
#                     h=m-1
#                 else:
#                     l= m
#             return -1
                
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l
        l, r = 0, len(nums) - 1

        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1