class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        maxHeap = []
        for point in points:
            dist = point[0]**2 + point[1]**2
            heapq.heappush(maxHeap, (-dist, point[0], point[1]))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        return [[point[1], point[2]] for point in maxHeap]