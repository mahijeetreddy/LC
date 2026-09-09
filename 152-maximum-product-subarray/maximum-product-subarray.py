class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1, 1
        res = max(nums)

        for n in nums:
            if n == 0 :
                curMin, curMax = 1,1
                continue
            tmp = curMax*n
            curMax = max(curMax*n, curMin*n, n)
            curMin = min(tmp, curMin*n, n)
            res = max(res, curMin, curMax)
        return res