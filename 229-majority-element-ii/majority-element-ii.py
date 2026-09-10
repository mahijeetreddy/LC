class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        threshold = n//3
        res = []
        count = Counter(nums)
        for n in nums:
            if count[n] > threshold:
                if n not in res:
                    res.append(n)
        return res