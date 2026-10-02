"""
2096. Step-By-Step Directions From a Binary Tree Node to Another
Difficulty: Medium
https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

──────────────────────────────────────────────────

You are given the root of a binary tree with n nodes. Each node is
uniquely assigned a value from 1 to n. You are also given an integer
startValue representing the value of the start node s, and a different
integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t.
Generate step-by-step directions of such path as a string consisting
of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates
a specific direction:

	• 'L' means to go from a node to its left child node.

	• 'R' means to go from a node to its right child node.

	• 'U' means to go from a node to its parent node.

Return the step-by-step directions of the shortest path from node s
to node t.

 

Example 1:

Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 &rarr; 1 &rarr; 5 &rarr; 2
&rarr; 6.

Example 2:

Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 &rarr; 1.

 

Constraints:

	• The number of nodes in the tree is n.

	• 2 <= n <= 10^5

	• 1 <= Node.val <= n

	• All the values in the tree are unique.

	• 1 <= startValue, destValue <= n

	• startValue != destValue
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: TreeNode | None, startValue: int, destValue: int) -> str:
        parent = {root.val: (None, None)}
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                parent[node.left.val] = (node.val, 'L')
                stack.append(node.left)
            if node.right:
                parent[node.right.val] = (node.val, 'R')
                stack.append(node.right)

        def path_to(val):
            path = []
            while val is not None:
                path.append(val)
                val = parent[val][0]
            path.reverse()
            return path

        ps = path_to(startValue)
        pd = path_to(destValue)
        i = 0
        while i < len(ps) and i < len(pd) and ps[i] == pd[i]:
            i += 1
        res = ['U'] * (len(ps) - i)
        for j in range(i, len(pd)):
            res.append(parent[pd[j]][1])
        return ''.join(res)
