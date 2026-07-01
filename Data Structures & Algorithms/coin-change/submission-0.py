class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Size amount + 1, that is filled with amount + 1 value (placeholder)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 # Base case: it takes 0 coin to make the amount 0

        for a in range(1, amount + 1):
            for c in coins:
                # If amount - coin does not go negative
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1
