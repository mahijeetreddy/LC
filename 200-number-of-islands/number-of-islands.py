class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visit = set()

        def dfs(r,c):
            if (r<0 or c<0 or r == ROWS or c == COLS or grid[r][c] == "0" or (r,c) in visit):
                return
            directions = [[0,1], [1,0],[0,-1],[-1,0]]
            visit.add((r,c))

            for dr, dc in directions:
                row, col = r + dr, c + dc
                dfs(row, col)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    islands+=1
                    dfs(r,c)
        return islands