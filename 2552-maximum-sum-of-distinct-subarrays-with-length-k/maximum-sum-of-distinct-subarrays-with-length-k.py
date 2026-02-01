class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = collections.defaultdict(int)
        l = 0
        curr_sum = 0
        res = 0
        for r in range(len(nums)):
            window[nums[r]] +=1
            curr_sum += nums[r]

            if r-l+1>k:
                window[nums[l]] -=1
                curr_sum -= nums[l]
                if window[nums[l]] == 0:
                    del window[nums[l]]
                l+=1
            if r-l+1 == k and len(window) == k:
                res = max(res, curr_sum)
        return res