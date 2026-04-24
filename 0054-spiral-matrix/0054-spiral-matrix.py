class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        r = len(matrix[0])
        l = -1
        u = -1
        d = len(matrix)
        o = []

        while l+1<r and u+1<d:

            for i in range(l+1,r):
                o.append(matrix[u+1][i])
            u+=1
            # if u+1 >= d:
            #     break

            for i in range(u+1,d):
                o.append(matrix[i][r-1])
            r -=1
            # if l +1>= r:
            #     break

            for i in range(r-1, l, -1):
                o.append(matrix[d-1][i])
            d -=1
            # if u+1 >= d:
            #     break

            for i in range(d-1,u,-1):
                o.append(matrix[i][l+1])
            l +=1
            # if l>=r:
            #     break
            
        return o