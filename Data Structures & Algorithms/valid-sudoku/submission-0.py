class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use for checking for duplicates
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squ = collections.defaultdict(set) # key = (r//3, c//3)

        for r in range(9):
            for c in range(9):
                
                # Check if empty
                if board[r][c] == ".":
                    continue
                
                # Check if this number appear before for rows, cols, and square
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squ[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squ[(r // 3, c // 3)].add(board[r][c])
        
        return True