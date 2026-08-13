class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, a in enumerate(nums):
            complement = target - a
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[a] = i