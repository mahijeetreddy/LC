class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        output = [intervals[0]]
        for start, end in intervals:
            lastEnd = output[-1][1]
            if start<= lastEnd:
                output[-1][1] = max(end, lastEnd)
            else:
                output.append([start, end])
        return output