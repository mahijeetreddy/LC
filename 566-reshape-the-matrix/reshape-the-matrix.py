class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        l = 0
        newmat = [[0]*c for _ in range(r)]
        ROWS, COLS = len(mat), len(mat[0])
        if ROWS * COLS != r*c:
            return mat

        for i in range(r):
            for j in range(c):
                old_row = l// COLS
                old_col = l% COLS

                newmat[i][j] = mat[old_row][old_col]

                l+=1
        return newmat