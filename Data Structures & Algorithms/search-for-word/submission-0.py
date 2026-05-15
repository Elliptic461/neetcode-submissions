class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # runtime: O(m * (4^n))
        rows, cols = len(board), len(board[0])
        # Make sure we don't revisit the same block, so we use set
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            # Checking if out of bound, revisit the same character twice, or word not matching on the board
            if (r < 0 or c < 0 or r >= rows or c >= cols
                or word[i] != board[r][c] or (r, c) in path):
                return False
            
            path.add((r, c))
            # Check all direction
            result = (dfs(r + 1, c, i + 1) or
                                dfs(r - 1, c, i + 1) or
                                dfs(r, c + 1, i + 1) or
                                dfs(r, c - 1, i + 1))
            # Clear up
            path.remove((r, c))
            return result
        
        # Brute force every 
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True
        return False

