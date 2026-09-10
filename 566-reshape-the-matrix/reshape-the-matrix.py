class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        arr = []
        l = 0
        newmat = [[0]*c for _ in range(r)]
        ROWS, COLS = len(mat), len(mat[0])
        for i in range(ROWS):
            for j in range(COLS):
                arr.append(mat[i][j])
        if len(arr) != r*c:
            return mat
        
        for i in range(r):
            for j in range(c):
                newmat[i][j] = arr[l]
                l+=1
        return newmat