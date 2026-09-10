class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) // 3
        count = Counter(nums)

        res = []

        for num, freq in count.items():
            if freq > threshold:
                res.append(num)

        return res
