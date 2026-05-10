# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Store the max path sum
        result = [root.val]

        # Return max path sum without split
        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right) 
            # If negative, don't take that path.
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0) 

            # Compute max path sum with split
            result[0] =  max(result[0], root.val + leftMax + rightMax)

            # Return value without splitting
            return root.val + max(leftMax, rightMax) 
        
        dfs(root) 
        return result[0]
