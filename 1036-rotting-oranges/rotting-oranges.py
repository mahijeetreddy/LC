class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        minutes = 0
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1
                elif grid[r][c] == 2:
                    q.append((r,c))
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        while q and fresh>0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    row = dr + r
                    col = dc + c
                    if (0<=row< ROWS  and 0<= col<COLS and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -=1
            minutes +=1
        return minutes if fresh == 0 else -1

