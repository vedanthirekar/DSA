class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        seen = {}

        for i,number in enumerate(numbers):
            complement = target -number
            if complement in seen and seen[complement]<i:
                return [seen[complement]+1,i+1]
            
            seen[number] = i