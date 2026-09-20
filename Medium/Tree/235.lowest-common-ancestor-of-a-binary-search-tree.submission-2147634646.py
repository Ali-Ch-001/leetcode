# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        
        while curr:
            # If both target nodes are smaller, LCA must be in the left subtree
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # If both target nodes are greater, LCA must be in the right subtree
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # The split point: one node is to the left, one is to the right,
            # or current node equals p or q. This is the LCA.
            else:
                return curr