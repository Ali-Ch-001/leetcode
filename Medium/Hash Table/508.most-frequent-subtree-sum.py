"""
508. Most Frequent Subtree Sum
Difficulty: Medium
https://leetcode.com/problems/most-frequent-subtree-sum/

──────────────────────────────────────────────────

Given the root of a binary tree, return the most frequent subtree
sum. If there is a tie, return all the values with the highest
frequency in any order.

The subtree sum of a node is defined as the sum of all the node
values formed by the subtree rooted at that node (including the node
itself).

 

Example 1:

Input: root = [5,2,-3]
Output: [2,-3,4]

Example 2:

Input: root = [5,2,-5]
Output: [2]

 

Constraints:

	• The number of nodes in the tree is in the range [1, 10^4].

	• -10^5 <= Node.val <= 10^5
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode | None) -> list[int]:
        counts = {}

        def dfs(node: TreeNode | None) -> int:
            if not node:
                return 0
            total = node.val + dfs(node.left) + dfs(node.right)
            counts[total] = counts.get(total, 0) + 1
            return total

        dfs(root)
        if not counts:
            return []
        best = max(counts.values())
        return [value for value, count in counts.items() if count == best]
