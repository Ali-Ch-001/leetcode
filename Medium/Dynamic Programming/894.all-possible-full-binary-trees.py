"""
894. All Possible Full Binary Trees
Difficulty: Medium
https://leetcode.com/problems/all-possible-full-binary-trees/

──────────────────────────────────────────────────

Given an integer n, return a list of all possible full binary trees
with n nodes. Each node of each tree in the answer must have Node.val
== 0.

Each element of the answer is the root node of one possible tree. You
may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or
2 children.

 

Example 1:

Input: n = 7
Output:
[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]

Example 2:

Input: n = 3
Output: [[0,0,0]]

 

Constraints:

	• 1 <= n <= 20
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> list[TreeNode | None]:
        if n % 2 == 0:
            return []
        memo = {1: [TreeNode(0)]}
        for size in range(3, n + 1, 2):
            trees = []
            for left_size in range(1, size - 1, 2):
                right_size = size - 1 - left_size
                for left in memo[left_size]:
                    for right in memo.get(right_size, []):
                        trees.append(TreeNode(0, left, right))
            memo[size] = trees
        return memo[n]
