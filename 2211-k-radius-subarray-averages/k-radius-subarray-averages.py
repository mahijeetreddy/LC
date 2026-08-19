class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        avg = [-1] * n
        if k == 0:
            return nums
        window_size = 2*k + 1
        if window_size > n:
            return avg
        windowSum = sum(nums[:window_size])
        avg[k] = windowSum // window_size

        for i in range(k+1, n-k):
            windowSum -= nums[i-k-1]
            windowSum += nums[k+i]
            avg[i] = windowSum // window_size
        return avg