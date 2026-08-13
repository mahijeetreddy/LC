from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter() # Dict -> {}
        for n in nums:
            freq[n] +=1
        # { 1:3, 2:2, 3:1}

        arr = list(freq.items())
        arr.sort(key=lambda x: x[1], reverse= True)
        res = []
        for i in range(k):
            res.append(arr[i][0])
        return res
