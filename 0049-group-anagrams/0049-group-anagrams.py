class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = defaultdict(list)
        for s in strs:
            charset = [0]*26
            for i in s:
                charset[ord(i)-97] +=1
            
            dictt[tuple(charset)].append(s)

        l = []
        for k in dictt:
            l.append(dictt[k])

        return l
        # return dictt[key] for key in dictt 