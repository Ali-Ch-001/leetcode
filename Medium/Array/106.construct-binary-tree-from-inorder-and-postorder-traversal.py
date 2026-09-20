"""
106. Construct Binary Tree from Inorder and Postorder Traversal
Difficulty: Medium
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

──────────────────────────────────────────────────

Given two integer arrays inorder and postorder where inorder is the
inorder traversal of a binary tree and postorder is the postorder
traversal of the same tree, construct and return the binary tree.

 

Example 1:

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]

 

Constraints:

	• 1 <= inorder.length <= 3000

	• postorder.length == inorder.length

	• -3000 <= inorder[i], postorder[i] <= 3000

	• inorder and postorder consist of unique values.

	• Each value of postorder also appears in inorder.

	• inorder is guaranteed to be the inorder traversal of the tree.

	• postorder is guaranteed to be the postorder traversal of the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        index = {value: i for i, value in enumerate(inorder)}

        def build(in_start: int, in_end: int, post_start: int, post_end: int) -> TreeNode | None:
            if in_start > in_end:
                return None
            root_value = postorder[post_end]
            root = TreeNode(root_value)
            split = index[root_value]
            left_size = split - in_start
            root.left = build(in_start, split - 1, post_start, post_start + left_size - 1)
            root.right = build(split + 1, in_end, post_start + left_size, post_end - 1)
            return root

        return build(0, len(inorder) - 1, 0, len(postorder) - 1)
