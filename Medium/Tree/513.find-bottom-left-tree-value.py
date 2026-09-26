"""
513. Find Bottom Left Tree Value
Difficulty: Medium
https://leetcode.com/problems/find-bottom-left-tree-value/

──────────────────────────────────────────────────

You are given the root of a binary tree.

Return the leftmost value in the last row of the tree.

 

Example 1:

Input: root = [2,1,3]
Output: 1
Explanation: The last row is [1,3], so the leftmost value is 1.

Example 2:

Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
Explanation: The last row contains only the node 7.

 

Constraints:

	• The number of nodes in the tree is in the range [1, 10^4].

	• -2^31 <= Node.val <= 2^31 - 1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        queue = deque([root])
        result = root.val
        while queue:
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
            result = node.val
        return result
