class Solution:
    def countBits(self, n: int) -> List[int]:
        # res = []
        # count = 0
        # for i in range(n+1):
        #     count = 0
        #     while i>0:
        #         if i%2==1:
        #             count +=1
        #         i = i//2 
        #     res.append(count)
        # return res
                 
        dp= [0]*(n+1)
        offset = 1
        for i in range(1,n+1):
            if offset*2 == i:
                offset = i
            dp[i] = 1+dp[i-offset]

        return dp