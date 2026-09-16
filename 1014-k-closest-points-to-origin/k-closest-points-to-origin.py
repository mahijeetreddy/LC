class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        minHeap = []
        output = []
        
        for i, point in enumerate(points):
            dist = point[0]**2 + point[1]**2
            heapq.heappush(minHeap, [dist, point[0], point[1]])
        
        for i in range(k):
            val = heapq.heappop(minHeap)
            output.append([val[1], val[2]])
        return output


