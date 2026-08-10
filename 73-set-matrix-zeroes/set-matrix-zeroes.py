class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        zeroes = []
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    zeroes.append((i,j))
        def dfs(r,c):
            for x in range(ROWS):
                matrix[x][c] = 0
            for y in range(COLS):
                matrix[r][y] = 0

        for r,c in zeroes:
            dfs(r,c)