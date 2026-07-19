class CountSquares:

    def __init__(self):
        # Default value is 0 
        self.ptsCount = defaultdict(int)
        self.pts = []

        
    # Runtime: O(n)
    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)
        
    # Runtime: O(n)
    def count(self, point: List[int]) -> int:
        result = 0
        px, py = point

        # All possible diagonal
        for x, y in self.pts:
            #Checking if they are diagonal to each other
            # Also checking if the points are on top of each other
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            
            result += self.ptsCount[(x, py)] *self.ptsCount[(px, y)]
        
        return result
            


        
