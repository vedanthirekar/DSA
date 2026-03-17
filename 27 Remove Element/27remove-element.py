class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        z = 0
        n = len(nums)
        x = n-1
        count = 0
        while z<=x:
            if nums[z] == val:
                nums[z], nums[x] = nums[x], nums[z]
                x -=1

            else:
                z += 1
                # count +=1

        print(nums)
        return z
            