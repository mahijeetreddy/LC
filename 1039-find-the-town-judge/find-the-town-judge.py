class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        incoming, outgoing = defaultdict(int), defaultdict(int)

        for src, dst in trust:
            outgoing[src] = outgoing[src] + 1
            incoming[dst] +=1
        
        for i in range(1, n+1):
            if outgoing[i] == 0 and incoming[i] == n - 1:
                return i
        return -1