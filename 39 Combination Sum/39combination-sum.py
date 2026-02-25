# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # cand = []
        # ans = []
        # n = len(candidates)
        # total = 0

        # def bt(start, total):
        #     if  total == target:
        #         ans.append(cand[:])
        #         return

        #     if total > target:
        #         return

        #     for i in range(start,n):
        #             # cand.pop(0)
        #             cand.append(candidates[i])
        #             bt(i,total+candidates[i])
        #             cand.pop()

        # bt(0,0)
        # return ans
        
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cand = []
        ans = []

        def bt(start):
            if sum(cand) == target:
                ans.append(cand[:])
                return
            if sum(cand) > target:
                return

            for i in range(start, len(candidates)):
                cand.append(candidates[i])
                bt(i)        # i, not i+1 — same number can be reused
                cand.pop()

        bt(0)
        return ans