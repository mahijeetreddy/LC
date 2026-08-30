class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        output = float("inf")
        l = 0
        winsum = 0
        for r in range(len(nums)):
            winsum += nums[r]
            while winsum >= target:
                output = min(output, r - l + 1)
                winsum -= nums[l]
                l += 1
        return 0 if output == float("inf") else output