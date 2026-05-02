class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows, Cols = len(matrix), len(matrix[0])

        top, bottom = 0, Rows - 1

        # Find which row has the target.
        # O(log(m))
        while top <= bottom:
            midRow = (top + bottom) // 2

            if target > matrix[midRow][-1]:
                top = midRow + 1
            elif target < matrix[midRow][0]:
                bottom = midRow - 1
            else:
                # target == matrix[midRow][0]
                # target == matrix[midRow][-1]
                break
        
        if not (top <= bottom):
            return False

        rowFound = (top + bottom) // 2
        left, right = 0, Cols - 1
        # Find target in the current row
        # O(log(n))
        while left <= right:
            mid = (left + right) // 2
            
            if target > matrix[rowFound][mid]:
                left = mid + 1
            elif target < matrix[rowFound][mid]:
                right = mid - 1
            else:
                return True
        
        # Runtime: O(log(m*n))
        return False
        
