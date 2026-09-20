class Solution:
    def minimumPushes(self, word: str) -> int:
        summ = 0
        for i in range(len(word)):
            summ += i//8 + 1

        return summ