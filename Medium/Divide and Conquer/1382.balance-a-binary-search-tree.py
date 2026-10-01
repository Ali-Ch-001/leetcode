"""
1382. Balance a Binary Search Tree
Difficulty: Medium
https://leetcode.com/problems/balance-a-binary-search-tree/

──────────────────────────────────────────────────

Given the root of a binary search tree, return a balanced binary
search tree with the same node values. If there is more than one
answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of
every node never differs by more than 1.

 

Example 1:

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is
also correct.

Example 2:

Input: root = [2,1,3]
Output: [2,1,3]

 

Constraints:

	• The number of nodes in the tree is in the range [1, 10^4].

	• 1 <= Node.val <= 10^5
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode | None) -> TreeNode | None:
        vals = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)

        inorder(root)

        def build(lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            node = TreeNode(vals[mid])
            node.left = build(lo, mid - 1)
            node.right = build(mid + 1, hi)
            return node

        return build(0, len(vals) - 1)
        
