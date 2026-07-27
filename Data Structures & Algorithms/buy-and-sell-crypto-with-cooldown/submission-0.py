class Solution:
    # Runtime: O(n)
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or selling?
        # If buy -> i + 1
        # If Sell -> i + 2, + 2 because of cooldown after selling it

        dp = {} # key = (i, buying (boolean)), val = max_profit

        def dfs(i, buying):
            # If it is out of bound
            if i >= len(prices):
                return 0
            
            # If we already computed this
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                # If we are buying, subtract the price of what we bought
                buy = dfs(i + 1, not buying) - prices[i]
                # If we are waiting, just skip
                cooldown = dfs(i + 1, buying)
                # Take the max of the two
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]
        
        return dfs(0, True)



        