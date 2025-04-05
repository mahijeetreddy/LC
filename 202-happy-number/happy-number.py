class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            ns = str(n)
            sum = 0
            for i in ns:
                sum += int(i) ** 2
            n = sum

        return n == 1