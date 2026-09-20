# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Fast exit: empty node or matched target
        if not root or root is p or root is q:
            return root

        # Search left subtree
        left = self.lowestCommonAncestor(root.left, p, q)

        # Early-pruning: if left is already the LCA (not p, not q), skip right subtree entirely
        if left and left is not p and left is not q:
            return left

        # Search right subtree only when necessary
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both sides returned a target, root is the LCA; otherwise propagate the found node
        return root if left and right else (left or right)