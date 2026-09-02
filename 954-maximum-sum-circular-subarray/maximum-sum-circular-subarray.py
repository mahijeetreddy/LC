class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        def maxKadane(nums):
            maxSub = nums[0]
            curSum = 0

            for n in nums:
                if curSum<0:
                    curSum = 0
                curSum +=n
                maxSub = max(maxSub, curSum)
            return maxSub

        def minKadane(nums):
            minSub = nums[0]
            curSum = 0

            for n in nums:
                if curSum>0:
                    curSum = 0
                curSum +=n
                minSub = min(minSub, curSum)
            return minSub

        maxSum = maxKadane(nums)
        if maxSum <0:
            return maxSum
        total = sum(nums)
        minSum = minKadane(nums)

        return max(maxSum, total - minSum)

        