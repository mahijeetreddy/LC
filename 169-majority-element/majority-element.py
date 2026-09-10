class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        threshold = n//2
        count = Counter(nums)

        for n in nums:
            if count[n] > threshold:
                return n
