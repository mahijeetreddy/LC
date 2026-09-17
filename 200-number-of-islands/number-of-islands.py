class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c):
            if (r<0 or c< 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == "0"):
                return
            visit.add((r,c))
            directions = [[0,1],[1,0],[0,-1],[-1,0]]
            for dr,dc in directions:
                row = dr + r
                col = dc + c
                dfs(row, col)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] == "1":
                    islands +=1
                    dfs(r,c)
        return islands