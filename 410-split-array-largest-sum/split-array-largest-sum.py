class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l,r = max(nums), sum(nums)

        def canSplit(largest):
            subarrays = 1
            currSum = 0
            for n in nums:
                currSum +=n
                if currSum> largest:
                    subarrays +=1
                    currSum = n
            return subarrays <= k

        while l<=r:
            mid = l + ((r-l)//2)

            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res