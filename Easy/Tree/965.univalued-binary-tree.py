"""
965. Univalued Binary Tree
Difficulty: Easy
https://leetcode.com/problems/univalued-binary-tree/

──────────────────────────────────────────────────

A binary tree is uni-valued if every node in the tree has the same
value.

Given the root of a binary tree, return true if the given tree is
uni-valued, or false otherwise.

 

Example 1:

Input: root = [1,1,1,1,1,null,1]
Output: true

Example 2:

Input: root = [2,2,2,5,2]
Output: false

 

Constraints:

	• The number of nodes in the tree is in the range [1, 100].

	• 0 <= Node.val < 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode | None) -> bool:
        value = root.val
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val != value:
                return False
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return True
