"""
222. Count Complete Tree Nodes
Difficulty: Medium
https://leetcode.com/problems/count-complete-tree-nodes/

──────────────────────────────────────────────────

Given the root of a complete binary tree, return the number of the
nodes in the tree.

According to Wikipedia, every level, except possibly the last, is
completely filled in a complete binary tree, and all nodes in the last
level are as far left as possible. It can have between 1 and 2^h nodes
inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:

Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:

Input: root = []
Output: 0

Example 3:

Input: root = [1]
Output: 1

 

Constraints:

	• The number of nodes in the tree is in the range [0, 5 * 10^4].

	• 0 <= Node.val <= 5 * 10^4

	• The tree is guaranteed to be complete.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        def depth(node: TreeNode | None) -> int:
            d = 0
            while node:
                d += 1
                node = node.left
            return d

        left_depth = depth(root.left)
        right_depth = depth(root.right)
        if left_depth == right_depth:
            return (1 << left_depth) + self.countNodes(root.right)
        return (1 << right_depth) + self.countNodes(root.left)
