class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        n = len(arr)
        windowSum = sum(arr[:k])
        windowAvg = windowSum//k
        if windowAvg >= threshold:
            res +=1
        for i in range(0,n-k):
            windowSum -=arr[i]
            windowSum += arr[i+k]
            if windowSum >= threshold * k:
                res+=1
        return res