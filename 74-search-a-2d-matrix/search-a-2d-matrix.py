class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        #find row
        while top<= bottom:
            midrow = (top + bottom)//2

            if target > matrix[midrow][-1]:
                top = midrow + 1
            elif target < matrix[midrow][0]:
                bottom = midrow - 1
            else:
                break
        if top > bottom:
            return False

        row = (top + bottom)//2
        
        while l<=r:
            mid = (l+r)//2
            if target < matrix[row][mid]:
                r = mid - 1
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                return True
        return False
