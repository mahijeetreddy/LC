class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        t,b, l, r = 0, len(matrix)-1, 0, len(matrix[0]) - 1

        while t<=b:
            midrow = (t+b)//2

            if target > matrix[midrow][-1]:
                t = midrow + 1
            elif target < matrix[midrow][0]:
                b = midrow - 1
            else: break
        else:
            return False

        while l<=r:
            mid = (l+r)//2
            if matrix[midrow][mid] == target:
                return True
            elif target < matrix[midrow][mid]:
                r = mid - 1
            else:
                l = mid + 1
        return False