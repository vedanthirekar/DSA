class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures 
        stk = [(t[0],0)]
        li = [0]*len(t)
        for i in range(1,len(temperatures)):
            while stk and t[i]>stk[-1][0]:
                a = stk.pop()
                li[a[1]] = i-a[1]

            stk.append((t[i],i))

            
        return li

        # stk = []  # stack of indices
        # li = [0] * len(temperatures)

        # for i, temp in enumerate(temperatures):
        #     while stk and temp > temperatures[stk[-1]]:
        #         idx = stk.pop()
        #         li[idx] = i - idx
        #     stk.append(i)

        # return li