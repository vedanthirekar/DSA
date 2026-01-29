class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        print(count)

        for r in ransomNote:
            if r in count and count[r]>0:
                count[r] -= 1
            else:
                return False
        return True
        