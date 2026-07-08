class Solution:
    # Runtime: O(E*k), e is the edge, k is the stops 
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Use bellman-ford 
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy() # Use to determine whether we can take the path if we are allow k stop
            for s, d, p in flights: # s=source, d = desination, p = price
            # We can reach this node
                if prices[s] == float("inf"):
                    continue
                # Found path to desination node that is cheaper
                if prices[s] + p  < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            
            prices = tmpPrices
        
        return prices[dst] if prices[dst] != float("inf") else -1




        