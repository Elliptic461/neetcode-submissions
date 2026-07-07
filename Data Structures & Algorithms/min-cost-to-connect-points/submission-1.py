class Solution:
    # Runtime: O((n^2)*log(n))
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        # Create adj list
        adj = {i:[] for i in range(N)} # i :  list of [cost, node]

        # Get the edges for every node to all the other nodes
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        # Prim's algorithm
        result = 0
        visit = set()
        minHeap = [[0, 0]] # [cost, point]

        while len(visit) < N:
            cost, i = heapq.heappop(minHeap)
            # If we already visit this node
            if i in visit:
                continue
            
            result += cost
            visit.add(i)
            
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCost, nei])
        
        return result








        