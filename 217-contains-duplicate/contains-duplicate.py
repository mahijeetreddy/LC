class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = set()
        for n in nums:
            if n in numset:
                return True
            if n not in numset:
                numset.add(n)
        return False