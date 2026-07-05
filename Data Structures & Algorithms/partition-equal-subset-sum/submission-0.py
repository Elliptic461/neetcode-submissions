class Solution:
    # Runtime: O(n * sum)
    def canPartition(self, nums: List[int]) -> bool:
        # If the total sum is odd you can't split it into two equal halves, because an odd number divided by
        # 2 isn't a whole number and all elements are integers, any subset sum will always be a whole number
        if sum(nums) % 2 != 0:
            return False

        # The target each subset needs to sum to
        target = sum(nums) // 2
        dp = {0} # set of all reachable sums so far, ex: 0 is reachable by picking no elements, which sums to 0

        # For each number n, compute all new reachable nums by either including or skipping n
        # for every sum already in dp
        for n in nums:
            # Use separate next_dp to avoid using the same number twice in one pass
            next_dp = set()
            for val in dp:
                # Include n
                next_dp.add(val + n)
                # Skip n
                next_dp.add(val)
            
            dp = next_dp
        
        return target in dp
        