from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mins = 0
        fresh = 0
        q = deque()

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh +=1
                elif grid[r][c] == 2:
                    q.append((r,c))

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while q and fresh >0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if (0<=row< ROWS and 0<= col < COLS and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -=1
            mins +=1
        return mins if fresh == 0 else -1
