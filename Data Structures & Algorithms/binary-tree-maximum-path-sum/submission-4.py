# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = root.val

        def dfs(curr):
            nonlocal result
            if not curr:
                return 0
            
            leftMax = dfs(curr.left)
            rightMax = dfs(curr.right)

            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            result = max(result, leftMax + rightMax + curr.val)

            return curr.val + max(leftMax, rightMax)

        dfs(root)
        return result
        