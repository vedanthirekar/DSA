class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        normally the solution would have been xor + &<<1. but in python, if the integer goes beyond 32 bit,
        it will not overflow and not ignore it. this creates a problem for this solution as this approach might keep
        on going forever (in normal case, at one point there is no carry and therefore b becomes 0 and loop stops).
        Here, after reading about it, i found that a mask needs to be applied to restrict it from running infinitely. 
        """

        mask = 0xFFFFFFFF  # 32-bit mask

        while b & mask:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        # if b is 0, a is the answer
        # if b still has bits beyond 32, a is a negative number
        return a if b == 0 else ~(a ^ mask)