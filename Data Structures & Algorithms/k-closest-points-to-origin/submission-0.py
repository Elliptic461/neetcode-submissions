class Solution:
    # Runtime: k*log(n)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        result = []
    
        for x, y in points:
            dist = (x ** 2) + (y**2)
            # For minHeap, it will use its first value (dist) to determine where to place it
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)

        # Pop the k closest points to the origin
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            result.append([x,y])
            k -= 1
        
        return result