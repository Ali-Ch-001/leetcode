"""
105. Construct Binary Tree from Preorder and Inorder Traversal
Difficulty: Medium
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

──────────────────────────────────────────────────

Given two integer arrays preorder and inorder where preorder is the
preorder traversal of a binary tree and inorder is the inorder
traversal of the same tree, construct and return the binary tree.

 

Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]

 

Constraints:

	• 1 <= preorder.length <= 3000

	• inorder.length == preorder.length

	• -3000 <= preorder[i], inorder[i] <= 3000

	• preorder and inorder consist of unique values.

	• Each value of inorder also appears in preorder.

	• preorder is guaranteed to be the preorder traversal of the tree.

	• inorder is guaranteed to be the inorder traversal of the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        index = {value: i for i, value in enumerate(inorder)}

        def build(pre_start: int, pre_end: int, in_start: int, in_end: int) -> TreeNode | None:
            if pre_start > pre_end:
                return None
            root_value = preorder[pre_start]
            root = TreeNode(root_value)
            split = index[root_value]
            left_size = split - in_start
            root.left = build(pre_start + 1, pre_start + left_size, in_start, split - 1)
            root.right = build(pre_start + left_size + 1, pre_end, split + 1, in_end)
            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
