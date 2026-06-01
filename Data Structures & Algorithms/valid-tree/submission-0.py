class Solution:
    # Runtime: O(E + V)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        # a dictionary where each key is a node, and its value is a list of its neighbors
        adj = {i:[] for i in range(n) }
        visit = set()

        # go through every pair of node and edge
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)

            # Go through neighbor of i
            # If the other neighbor did not reach any node visited before, return true
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            
            return True
        
        return dfs(0, -1) and n == len(visit)
