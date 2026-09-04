class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = []
        for x, y in points:
            distance = x**2 + y**2

            heapq.heappush(d, (-distance, x,y))

            if len(d) >k:
                heapq.heappop(d)
        res = []
        for i in range(k):
            res.append(heapq.heappop(d)[1:])
        return res