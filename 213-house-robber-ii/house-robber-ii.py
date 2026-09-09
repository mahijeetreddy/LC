class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        def robber(nums):
            rob1, rob2 = 0,0
            for n in nums:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        return max(nums[0], robber(nums[1:]), robber(nums[:len(nums) - 1]))
