class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ex = n*(n+1) //2
        asum = sum(nums)
        return ex - asum