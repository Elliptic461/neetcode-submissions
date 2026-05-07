# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Runtime: O(log(n))
        # Goal is to find the split
        curr = root
        while curr:
            # If both value greater than current value, go right
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If both value less than current value, go left
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr