class Solution:
    # Runtime: O(n* a) where n is the number of coin and a is the given amount
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1 # There is one way to get the amount "0"

        for c in coins:
            for a in range(c, amount + 1): # amounts this coin can contribute to
                dp[a] += dp[a - c] # add combo to this coin, 
                # dp[a - c] represent the number of combinations that make up the leftover amount after you have committed to placing on coin
        
        return dp[amount]

    
    # Note:
    # Since coins are infinite, when you land on amount "a" using "c" coin, the remaining
    # a - c may also use "c" again. dp[a- c] handles this





        