class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        count = 0
        # print(s)
        for stone in stones:
            if stone in s:
                count += 1
        return count
        