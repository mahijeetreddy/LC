class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sett = set(nums)

        # for i in range(len(nums)+1):
        #     if i not in sett:
        #         return i
        sum= 0
        n = len(nums)
        for i in range(n+1):
            sum = sum + i
        for n in nums:
            sum = sum - n
        return sum
            
