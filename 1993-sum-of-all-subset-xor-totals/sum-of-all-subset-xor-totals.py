class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        grandsum = 0

        def subsets(nums):
            res = [[]]

            for num in nums:
                newsub = []
                for subset in res:
                    newsub.append(subset + [num])
                res += newsub
            return res



        subsetarrays = subsets(nums)

        for s in subsetarrays:
            if len(s) == 0:
                indi = 0
            elif len(s) == 1:
                indi = s[0]
            elif len(s) > 1:
                indi = s[0] ^ s[1]
                for c in s[2:]:
                    indi ^= c
            grandsum = grandsum + indi
        return grandsum