class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Left = buy, right = sell
        left = 0
        right = 1
        maxProfit = 0

        while right < len(prices):
            # Buy low, sell high 
            if prices[left] < prices[right]:
                # Sell the neetcoin and see if that is the max profit thus far
                maxProfit = max(maxProfit, prices[right] - prices[left])
                right += 1
            else:
                left = right
                right += 1
        
        return maxProfit