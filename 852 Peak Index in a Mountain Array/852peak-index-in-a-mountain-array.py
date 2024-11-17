class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0
        high = len(arr) - 1

        while low < high:
            mid = low + (high - low) // 2  # Calculate mid in each iteration

            if arr[mid] < arr[mid + 1]:  # Peak is in the right half
                low = mid + 1
            else:  # Peak is in the left half (including mid)
                high = mid

        return low
