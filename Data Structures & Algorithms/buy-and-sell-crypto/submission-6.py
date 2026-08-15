class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #l = buying
        maxProfit = 0 

        while r < len(prices):
            maxProfit = max(maxProfit, prices[r] - prices[l])
            
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                r += 1
        
        return maxProfit

        