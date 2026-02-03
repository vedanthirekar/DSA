class Solution:
    def calPoints(self, operations: List[str]) -> int:
        n = len(operations)
        i = 0
        s = []
        while i<n:
            o  = operations[i]
            # if o.isnum():
            #     s.append(o)
            #     i +=1
            if o == "+":
                s.append(s[-1]+s[-2])
            elif o == "C":
                if s: 
                    s.pop()
            elif o =="D":
                s.append(s[-1]*2)
            else:
                s.append(int(o))
           
            i += 1
        return sum(s)

