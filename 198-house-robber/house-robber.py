class Solution:
    def rob(self, nums: List[int]) -> int:
        i,j = 0,0
        for n in nums:
            temp = max(n + i, j)
            i = j
            j = temp
        return j