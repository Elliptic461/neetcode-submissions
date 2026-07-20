class Solution:
    # Runtime: O(n)
    def canJump(self, nums: List[int]) -> bool:
        # Moving the goal post
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            # Can this jump starting at position i >= goal
            # If we can reach the goal, update the goal post
            if i + nums[i] >= goal:
                goal = i 
        
        return True if goal == 0 else False

        