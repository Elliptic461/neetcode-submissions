class Solution:
    # Runtime: O(m*n)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False  # Initially represent that the first row has a zero

        # determine which rows/column need to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0  # Set first row to zero

                    if r > 0:
                        matrix[r][0] = 0  # Set first column to zero
                    else:
                        rowZero = True

        # Zero out most of them
        for r in range(1, ROWS):  # Skip 1st row and 1st column
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Zero out the 1st column
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # Zero out the 1st row
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
