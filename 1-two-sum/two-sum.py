class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}

        for i,n in enumerate(nums):
            complement = target - n
            if complement in mapp:
                return [mapp[complement], i]

            mapp[n] = i
        