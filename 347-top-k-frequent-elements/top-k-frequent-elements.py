class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        output = []

        freq = [[] for i in range(len(nums)+1)]

        for n,c in count.items():
            freq[c].append(n)

        for i in range(len(freq)-1, 0,-1):
            for n in freq[i]:
                output.append(n)
                if len(output) == k:
                    return output
