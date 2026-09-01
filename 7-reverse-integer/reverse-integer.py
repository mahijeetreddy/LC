class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647

        res = 0

        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            new_res = res * 10 + digit

            if new_res < MIN or new_res > MAX:
                return 0

            res = new_res

        return res