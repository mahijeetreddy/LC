class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque([(0,0, 1)])
        visit = set((0,0))
        direct = [[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
        while q:
            r,c, length = q.popleft()

            if (min(r,c) <0 or r == N or c == N or grid[r][c] == 1):
                continue
            if r == N - 1 and c == N - 1:
                return length
            for dr, dc in direct:
                
                row = dr + r
                col = dc + c
                if (row, col) not in visit:
                    q.append((row, col, length + 1))
                    visit.add((row, col))
        return -1