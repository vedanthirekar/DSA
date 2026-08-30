class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        res = []

        for s in strs:
            s_map = [0]*26

            for letter in s:
                s_map[ord(letter)-ord("a")] +=1

            groups[tuple(s_map)].append(s)

        for value in groups.values():
            res.append(value)

        return res