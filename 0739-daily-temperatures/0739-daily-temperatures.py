class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stk = []

        n = len(temperatures)
        res = [0]*n
        for i in range(n):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                # print(stk[-1], " ---", i )
                a = stk.pop()
                res[a] = i -a
                
                # print("while", res)

            stk.append(i)

            # print(res)

        return res