class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        def numberofliveneighborschecker(r,c):
            nonlocal ROWS, COLS
            number = 0
            directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]

            for dr, dc in directions:
                row = dr + r
                col = dc + c
                if 0<=row< ROWS and 0<=col< COLS:
                    if board[row][col] == 1 or board[row][col] == 2:
                        number +=1
            return number

        
        for r in range(ROWS):
            for c in range(COLS):
                number = numberofliveneighborschecker(r,c)

                if board[r][c] == 1 and (number < 2 or number>3):
                    board[r][c] = 2
                elif board[r][c] == 1 and (number == 2 or number == 3): continue
                elif board[r][c] == 0 and number == 3:
                    board[r][c] = 3
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1