"""
1372. Longest ZigZag Path in a Binary Tree
Difficulty: Medium
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

──────────────────────────────────────────────────

You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

	• Choose any node in the binary tree and a direction (right or left).

• If the current direction is right, move to the right child of the
current node; otherwise, move to the left child.

	• Change the direction from right to left or from left to right.

	• Repeat the second and third steps until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1. (A
single node has a length of 0).

Return the longest ZigZag path contained in that tree.

 

Example 1:

Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left ->
right).

Example 2:

Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left
-> right).

Example 3:

Input: root = [1]
Output: 0

 

Constraints:

	• The number of nodes in the tree is in the range [1, 5 * 10^4].

	• 1 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        ans = 0
        stack = [(root, 0, 0)]
        while stack:
            node, direction, length = stack.pop()
            if length > ans:
                ans = length
            if node.left:
                if direction == 2:
                    stack.append((node.left, 1, length + 1))
                else:
                    stack.append((node.left, 1, 1))
            if node.right:
                if direction == 1:
                    stack.append((node.right, 2, length + 1))
                else:
                    stack.append((node.right, 2, 1))
        return ans
        
