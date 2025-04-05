# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         if (math.pow(n, 1/4)) % 2 != 0:
#             return True
#         if n <= 0:
#             return False
#         v = math.pow(n, 1/4)
#         return v.is_integer() and int(v) ** 4 == n
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 4 == 0:
            n = n // 4
        return n == 1