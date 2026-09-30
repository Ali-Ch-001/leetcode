"""
1028. Recover a Tree From Preorder Traversal
Difficulty: Hard
https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

──────────────────────────────────────────────────

We run a preorder depth-first search (DFS) on the root of a binary
tree.

At each node in this traversal, we output D dashes (where D is the
depth of this node), then we output the value of this node.  If the
depth of a node is D, the depth of its immediate child is D + 1.  The
depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left
child.

Given the output traversal of this traversal, recover the tree and
return its root.

 

Example 1:

Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]

Example 2:

Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]

Example 3:

Input: traversal = "1-401--349---90--88"
Output: [1,401,null,349,88,90]

 

Constraints:

	• The number of nodes in the original tree is in the range [1, 1000].

	• 1 <= Node.val <= 10^9
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode | None:
        i, n = 0, len(traversal)
        stack = []
        while i < n:
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1
            val = 0
            while i < n and traversal[i].isdigit():
                val = val * 10 + int(traversal[i])
                i += 1
            node = TreeNode(val)
            while len(stack) > depth:
                stack.pop()
            if stack:
                parent = stack[-1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node
            stack.append(node)
        return stack[0]
