class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        prod = 1
        l = res = 0
        for r in range(len(nums)):
            prod = prod* nums[r]
            while prod>=k:
                prod//= nums[l]
                l+=1
            res += (r-l+1)
        return res