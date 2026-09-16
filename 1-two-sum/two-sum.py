class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hmap = {}
        for i, a in enumerate(nums):
            complement = target - a
            if complement in hmap:
                return [hmap[complement], i]
            hmap[a] = i