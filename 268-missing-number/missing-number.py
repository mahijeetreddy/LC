class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sett = set(nums)

        for i in range(len(nums)+1):
            if i not in sett:
                return i
            
