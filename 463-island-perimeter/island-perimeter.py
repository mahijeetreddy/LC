class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        perimeter = 0
        visit = set()

        def dfs(r,c):
            nonlocal perimeter
            if r<0 or c<0 or r == ROWS or c == COLS or grid[r][c] == 0 or (r,c) in visit:
                return
            visit.add((r,c))
            directions = [[0,1],[1,0],[-1,0],[0,-1]]
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if 0<= row< ROWS and 0<= col < COLS:
                    if grid[row][col] == 1:
                        perimeter -=1
                        dfs(row, col)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    perimeter +=4
                    dfs(r,c)
        return perimeter