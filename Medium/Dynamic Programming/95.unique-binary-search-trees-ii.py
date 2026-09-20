"""
95. Unique Binary Search Trees II
Difficulty: Medium
https://leetcode.com/problems/unique-binary-search-trees-ii/

──────────────────────────────────────────────────

Given an integer n, return all the structurally unique BST's (binary
search trees), which has exactly n nodes of unique values from 1 to n.
Return the answer in any order.

 

Example 1:

Input: n = 3
Output:
[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:

Input: n = 1
Output: [[1]]

 

Constraints:

	• 1 <= n <= 8
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        def build(start: int, end: int) -> list[TreeNode | None]:
            if start > end:
                return [None]
            trees = []
            for root_value in range(start, end + 1):
                for left in build(start, root_value - 1):
                    for right in build(root_value + 1, end):
                        trees.append(TreeNode(root_value, left, right))
            return trees

        return build(1, n)
