class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i, n in enumerate(numbers):
            complement = target -n
            if complement in hashmap:
                return [hashmap[complement]+1, i+1]
            else:
                hashmap[n] = i
        