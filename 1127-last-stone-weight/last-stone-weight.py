class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-x for x in stones]
        heapq.heapify(minHeap)

        while len(minHeap) >= 2:
            a = -(heapq.heappop(minHeap))
            b = -(heapq.heappop(minHeap))
            diff = abs(a-b)
            if diff:
                heapq.heappush(minHeap, -diff)
        return -minHeap[0] if minHeap else 0