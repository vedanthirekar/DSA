class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        
        arr = [1]

        for x in range(rowIndex):
            arr = [0]+arr+[0]
            arr2 = []
            for i in range(len(arr)-1) :
                arr2.append(arr[i]+arr[i+1])

            arr = arr2

        return arr