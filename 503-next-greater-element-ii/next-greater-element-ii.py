class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        res = [-1] * n
        nums = nums* 2

        for i in range (0, n*2):
            while stack and nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                res[idx] = nums[i]
            if i < n:
                stack.append(i)
        return res
