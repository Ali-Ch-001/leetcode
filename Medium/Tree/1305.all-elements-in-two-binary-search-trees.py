"""
1305. All Elements in Two Binary Search Trees
Difficulty: Medium
https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

──────────────────────────────────────────────────

Given two binary search trees root1 and root2, return a list
containing all the integers from both trees sorted in ascending order.

 

Example 1:

Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:

Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]

 

Constraints:

	• The number of nodes in each tree is in the range [0, 5000].

	• -10^5 <= Node.val <= 10^5
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode | None, root2: TreeNode | None) -> list[int]:
        def inorder(root, out):
            if root is None:
                return
            inorder(root.left, out)
            out.append(root.val)
            inorder(root.right, out)

        a, b = [], []
        inorder(root1, a)
        inorder(root2, b)
        i = j = 0
        merged = []
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                merged.append(a[i])
                i += 1
            else:
                merged.append(b[j])
                j += 1
        merged.extend(a[i:])
        merged.extend(b[j:])
        return merged
