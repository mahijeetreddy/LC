class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i, a in enumerate(nums):
            complement = target - a
            if complement in hmap:
                return [hmap[complement], i]
            hmap[a] = i