class Solution:
    # Runtime: O(n^3)
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for length in range(1, n - 1):  # subarray length
            for l in range(1, n - 1 - length + 1):  # left boundary
                r = l + length - 1  # right boundary
                for i in range(l, r + 1):  # last balloon to pop
                    coins = nums[l - 1] * nums[i] * nums[r + 1]
                    coins += dp[l][i - 1] + dp[i + 1][r]
                    dp[l][r] = max(dp[l][r], coins)

        return dp[1][n - 2]
