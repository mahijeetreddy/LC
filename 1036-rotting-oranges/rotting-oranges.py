from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        mins = 0

        queue = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh +=1

        if fresh == 0:
            return 0

        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        while queue and fresh>0:
            level = len(queue)

            for _ in range(level):
                r,c = queue.popleft()

                for dr, dc in directions:
                    row = r+ dr
                    col = c + dc

                    if 0<= row< ROWS and 0 <= col < COLS:
                        if grid[row][col] == 1:
                            grid[row][col] = 2
                            fresh -=1
                            queue.append((row, col))
                    
            mins +=1

        if fresh >0:
            return -1
        
        return mins



