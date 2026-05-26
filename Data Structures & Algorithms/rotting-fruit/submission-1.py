class Solution:
    # Runtime: O(m*n)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        q =deque()
        time, fresh = 0, 0

        # Find all the rotten fruit 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            
            # Make all nearby orange rotten then adding up the time
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = dr + r, dc + c

                    # If in bounds and fresh, make rotten
                    if (row < 0 or row == rows or col < 0 or 
                            col == cols or grid[row][col] != 1):
                        continue
                    
                    grid[row][col] = 2
                    q.append([row, col]) 
                    fresh -= 1
            
            time += 1
    
        if fresh == 0:
            return time
        else:
            return -1
            



        
        