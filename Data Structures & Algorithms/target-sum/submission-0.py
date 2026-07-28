class Solution:
    # Runtime: O(n * m)
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {} # (index, cur_sum) -> num of ways

        def backtrack(i, cur_sum):
            # If we already compute it, then return the already computed result
            if (i, cur_sum) in dp:
                return dp[(i, cur_sum)]

            # If it reach the end of the array and it adds up to the target
            if i == len(nums):
                return 1 if cur_sum == target else 0
            
            dp[(i, cur_sum)] = (
                backtrack(i + 1, cur_sum + nums[i]) +
                backtrack(i + 1, cur_sum - nums[i])
            )
            
            return dp[(i, cur_sum)]
        
        return backtrack(0, 0)

        