# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Store max path sum 
        result = root.val
        
        def dfs(curr):
            nonlocal result
            if not curr:
                return 0 
            
            leftMax = dfs(curr.left)
            rightMax = dfs(curr.right)

            # If left or right came back negative, don't take the path and reset
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Compute max path sum with split
            result = max(result, curr.val + leftMax + rightMax)

            # That is because if the parent node is going extend the path
            # It can't visit left and right node's children without visiting the children twice
            # So take the child value plus the max of either left or right node's value
            return curr.val + max(leftMax, rightMax)

        dfs(root)
        return result
        




        