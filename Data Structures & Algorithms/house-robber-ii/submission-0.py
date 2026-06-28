class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge case: There is only one element in the array
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1])) # Skip first house and last house
        
    def helper(self, nums):
        rob1, rob2 = 0,0

        for n in nums:
            curr = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = curr
        return rob2
        