class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        threshold = n//3
        output = []
        count = Counter()
        for n in nums:
            count[n] +=1
        for n,c in count.items():
            if c> threshold:
                output.append(n)
        return output