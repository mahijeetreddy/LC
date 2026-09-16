class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        while top<= bottom:
            midrow = (top + bottom) //2

            if matrix[midrow][-1] < target:
                top = midrow + 1
            elif target < matrix[midrow][0]:
                bottom = midrow - 1
            else:
                break
        else:
            return False
        
        while left<=right:
            mid = (left + right)//2
            if matrix[midrow][mid] == target:
                return True
            elif target <= matrix[midrow][mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False