class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        total = len(nums1) + len(nums2)

        half = total//2

        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
        l = 0
        r = len(nums1)

        while True:
            i = l + (r-l)//2
            j = half - i 

            Aleft = nums1[i-1] if i>0 else float("-inf")
            Aright = nums1[i] if i<len(nums1) else float("inf")
            Bleft = nums2[j-1] if j>0 else float("-inf")
            Bright = nums2[j] if j<len(nums2) else float("inf")

            if Aleft<=Bright and Aright>=Bleft:
                if total%2 == 1:
                    return min(Aright,Bright)

                else:
                    return (max(Aleft,Bleft) + min(Aright,Bright))/2

            elif Aleft>Bright:
                r = i-1
            else:
                l = i+1