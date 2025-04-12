class Solution:
    def reverse(self, x: int) -> int:

        sign = -1 if x<0 else 1

        strr = str(abs(x))
        revs = strr[::-1]
        rever = sign * int(revs)
        
        if rever < -2**31 or rever > 2**31 - 1:
            return 0
        return rever

