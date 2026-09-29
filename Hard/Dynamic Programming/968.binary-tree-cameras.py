"""
968. Binary Tree Cameras
Difficulty: Hard
https://leetcode.com/problems/binary-tree-cameras/

──────────────────────────────────────────────────

You are given the root of a binary tree. We install cameras on the
tree nodes where each camera at a node can monitor its parent, itself,
and its immediate children.

Return the minimum number of cameras needed to monitor all nodes of
the tree.

 

Example 1:

Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as
shown.

Example 2:

Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of
the tree. The above image shows one of the valid configurations of
camera placement.

 

Constraints:

	• The number of nodes in the tree is in the range [1, 1000].

	• Node.val == 0
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode | None) -> int:
        cameras = 0
        NOT_COVERED, COVERED, HAS_CAMERA = 0, 1, 2

        def dfs(node):
            nonlocal cameras
            if not node:
                return COVERED
            left = dfs(node.left)
            right = dfs(node.right)
            if left == NOT_COVERED or right == NOT_COVERED:
                cameras += 1
                return HAS_CAMERA
            if left == HAS_CAMERA or right == HAS_CAMERA:
                return COVERED
            return NOT_COVERED

        if dfs(root) == NOT_COVERED:
            cameras += 1
        return cameras
