class Solution:
    def convertToBase7(self, num: int) -> str:
        og = num
        num = abs(num)
        rem = []

        if num ==0:
            return "0"

        while num>0:
            r = num%7
            rem.append(str(r))
            num //=7

        if og<0:
            rem.append("-")

        rem.reverse()
        return "".join(rem)