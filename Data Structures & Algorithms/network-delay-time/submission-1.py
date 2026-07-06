class Solution:
    # Runtime: O(ElogV)
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        # u is source node, v is target node, and w is the edge's weight
        for u, v, w in times:
            edges[u].append((v, w))
        
        # k is the node we start at
        minHeap = [(0, k)]
        visit = set()
        # t is result
        t = 0

        while minHeap:
            # Store weight and node in variable
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            
            # Add the node to visited set
            visit.add(n1)
            # See if this is the new minimum time
            t = max(t, w1)

            # Go through all the neighbor of n1 nodes
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        
        return t if len(visit) == n else -1
            

        