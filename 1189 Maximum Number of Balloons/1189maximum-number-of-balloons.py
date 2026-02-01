class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # count = Counter("balloon")
        # count 
        # for s in "balloon":
        # dict1 = {'b':0,'a':0, 'l':0, 'o':0, 'n':0}
        # dict2 = {}
        # for s in "balloon":
        #     dict2[s] = 0
        dict3 = defaultdict()
        for s in "balloon":
            dict3[s] = 0
        # print(dict3)
        for t in text:
            if t in dict3:
                dict3[t] +=1

        if any(c not in dict3 for c in "balloon"):
            return 0
        return(min(dict3['b'], dict3['a'], dict3['l']//2, dict3['o']//2, dict3['n']))
        # print(dict1, dict2)
        