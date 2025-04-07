class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        first = 1
        second = 2
        sum = 0
        while n>2:
            sum = first + second
            first = second
            second = sum
            n-=1
            
        return sum

