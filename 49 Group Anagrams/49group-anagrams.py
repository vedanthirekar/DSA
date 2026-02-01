class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_dict = defaultdict(list)

        for s in strs:
            k = [0]*26
            for c in s:
                k[ord(c)-ord('a')] +=  1

            key = tuple(k)
            anagram_dict[key].append(s)

        return list(anagram_dict.values())