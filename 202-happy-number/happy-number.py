class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def repsquare(n):
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            total = 0
            for c in str(n):
                total += int(c) ** 2
            return repsquare(total)
        return repsquare(n)