class Solution:
    # Runtime: O(n)
    def rob(self, nums: List[int]) -> int:

        rob1, rob2 = 0, 0 # dp[i - 2], dp[i - 1]

        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            curr = max(n + rob1, rob2)
            rob1 = rob2 
            rob2 = curr # updated to be "n" 
        return rob2


        