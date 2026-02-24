class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []

        def bt():
            if len(nums) == len(path):
                ans.append(path[:])
                return

            for i in nums:
                if i in path:
                    continue
                path.append(i)
                bt()
                path.pop()

        bt()
        return ans
