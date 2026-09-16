class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        res = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = res[-1][1]
            if start <= lastEnd:
                res[-1][1] = max(end, lastEnd)
            else:
                res.append([start,end])
        return res