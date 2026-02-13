class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        a = 0
        for i in range(k):
            a = heapq.heappop(nums)

        return -a 