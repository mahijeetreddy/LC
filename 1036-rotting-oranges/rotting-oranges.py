from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        mins = 0
        q = deque()

        ROWS, COLS = len(grid), len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh +=1
                elif grid[i][j] == 2:
                    q.append((i,j))
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while q and fresh>0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if (0<= row< ROWS and 0 <= col < COLS and grid[row][col] == 1):
                        grid[row][col] = 2
                        fresh -=1
                        q.append((row,col))
            mins +=1
        return mins if fresh == 0 else -1
