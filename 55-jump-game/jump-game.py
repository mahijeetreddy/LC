class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp = []
        # currJump = 0
        # for i in range(len(nums) - 2), -1, -1:
        #     currJump = nums[i]
        #     a = len(nums) - 2
        #     for x in range(currJump):
        #         a-=1
            

        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0