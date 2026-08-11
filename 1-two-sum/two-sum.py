class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashhmap = {}

        for i, a in enumerate(nums):
            complement = target - a

            if complement in hashhmap:
                return [hashhmap[complement], i]
            
            hashhmap[a] = i