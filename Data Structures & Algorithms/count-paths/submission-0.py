class Solution:
    # Runtime: O(m*n)
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n #  Bottom row: every cell has exactly 1 path to the corner (can only go right)
        
        # Iterate through each row 
        for i in range(m - 1): # Build rows from second-to-bottom up to the top (m-1 times; bottom row is already done)
            newRow = [1] * n # Start the current row; rightmost cell stays 1 (can only go down)
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j] # paths here = paths going right (newRow[j+1]) + paths going down (row[j])
            
            row = newRow # Current row becomes the "row below" for the next iteration up
        
        return row[0]

        