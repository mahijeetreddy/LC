class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False
        sq = math.pow(num, 1/2)
        return int(sq + 0.5)**2== num
