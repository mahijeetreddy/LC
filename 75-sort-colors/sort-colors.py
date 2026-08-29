class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mapp = Counter(nums)
        i = 0

        for color in range(3):
            for _ in range(mapp[color]):
                nums[i] = color
                i+=1