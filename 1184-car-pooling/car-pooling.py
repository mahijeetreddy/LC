class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minHeap = []
        current = 0
        trips.sort(key=lambda t:t[1])

        for people, start, end in trips:
            while minHeap and minHeap[0][0] <= start:
                end_time, passengers = heapq.heappop(minHeap)
                current -= passengers
            
            current += people
            if current > capacity:
                return False
            heapq.heappush(minHeap, (end, people))
        return True