class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        # Determine by (r+c)
        posDiag = set() 
        # Determine by (r - c)
        negDiag = set()

        result = []
        board = [["."] * n for i in range(n)]

        def backtrack(row):
            # If row reach the end of the board
            if row == n:
                copy = ["".join(r) for r in board]
                result.append(copy) 
                return
            
            for c in range(n):
                # If the queen is within another queens column or diagonal, skip it
                if c in col or (row+c) in posDiag or (row - c) in negDiag:
                    continue
                
                # You can place the queen, so place it and update
                col.add(c)
                posDiag.add(row + c)
                negDiag.add(row - c)
                board[row][c] = "Q"

                backtrack(row + 1)

                # Clean up for next iteration
                col.remove(c)
                posDiag.remove(row + c)
                negDiag.remove(row - c)
                board[row][c] = "."
        
        backtrack(0)
        return result
