class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        threshold = n//3
        res = []
        mapp = Counter(nums)

        for t,c in mapp.items():
            if c > threshold:
                res.append(t)
        return res