class Solution:
    # Runtime: O(ElogE)
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Map every source node to an empty list
        adj = {src: [] for src, dst in tickets}

        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)
        
        result = ["JFK"]
        def dfs(src):
            if len(result) == len(tickets) + 1:
                return True
            # No outgoing edges from source (src)
            if src not in adj:
                return False
            
            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                # add to our current path
                result.append(v)

                if dfs(v):
                    return True
                
                # Backtracking
                adj[src].insert(i, v)
                result.pop()
            return False
        
        dfs("JFK")
        return result




        