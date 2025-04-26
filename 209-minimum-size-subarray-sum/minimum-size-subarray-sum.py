class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # min_len = float('inf')
        # n = len(nums)
        # for i in range(n):
        #     sums= 0
        #     for j in range(i, n):
        #         sums += nums[j]
        #         if sums >= target:
        #             min_len = min(min_len, j-i+1)
        #             break
        # return 0 if min_len == float('inf') else min_len
        sums= 0
        left =0
        min_len = float('inf')

        for right in range(len(nums)):
            sums += nums[right]
            while sums >= target:
                min_len = min(min_len, right - left +1)
                sums -= nums[left]
                left +=1
        return 0 if min_len == float('inf') else min_len