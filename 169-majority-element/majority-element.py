# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         s = len(nums) // 2
        
#         for i in range(len(nums)):
#             count = 0
#             for j in range(len(nums)):
#                 if nums[i] == nums[j]:
#                     count += 1
#             if count > s:
#                 return nums[i]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = len(nums) // 2
        count_map = {}

        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
            if count_map[num] > s:
                return num
