class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        seen = Counter({0:1})
        for num in nums:
            prefix_sum += num
            count+= seen[prefix_sum - k]
            seen[prefix_sum] +=1
        return count