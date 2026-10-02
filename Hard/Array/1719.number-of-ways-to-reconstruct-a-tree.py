"""
1719. Number Of Ways To Reconstruct A Tree
Difficulty: Hard
https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/

──────────────────────────────────────────────────

You are given an array pairs, where pairs[i] = [xi, yi], and:

	• There are no duplicates.

	• xi < yi

Let ways be the number of rooted trees that satisfy the following
conditions:

	• The tree consists of nodes whose values appeared in pairs.

• A pair [xi, yi] exists in pairs if and only if xi is an ancestor
of yi or yi is an ancestor of xi.

	• Note: the tree does not have to be a binary tree.

Two ways are considered to be different if there is at least one node
that has different parents in both ways.

Return:

	• 0 if ways == 0

	• 1 if ways == 1

	• 2 if ways > 1

A rooted tree is a tree that has a single root node, and all edges
are oriented to be outgoing from the root.

An ancestor of a node is any node on the path from the root to that
node (excluding the node itself). The root has no ancestors.

 

Example 1:

Input: pairs = [[1,2],[2,3]]
Output: 1
Explanation: There is exactly one valid rooted tree, which is shown
in the above figure.

Example 2:

Input: pairs = [[1,2],[2,3],[1,3]]
Output: 2
Explanation: There are multiple valid rooted trees. Three of them are
shown in the above figures.

Example 3:

Input: pairs = [[1,2],[2,3],[2,4],[1,5]]
Output: 0
Explanation: There are no valid rooted trees.

 

Constraints:

	• 1 <= pairs.length <= 10^5

	• 1 <= xi < yi <= 500

	• The elements in pairs are unique.
"""

from collections import defaultdict


class Solution:
    def checkWays(self, pairs: list[list[int]]) -> int:
        g = defaultdict(set)
        for u, v in pairs:
            g[u].add(v)
            g[v].add(u)
        nodes = sorted(g, key=lambda x: -len(g[x]))
        n = len(nodes)
        if len(g[nodes[0]]) != n - 1:
            return 0
        ans = 1
        for i in range(1, n):
            v = nodes[i]
            parent = None
            for j in range(i - 1, -1, -1):
                if nodes[j] in g[v]:
                    parent = nodes[j]
                    break
            if parent is None:
                return 0
            for w in g[v]:
                if w != parent and w not in g[parent]:
                    return 0
            if len(g[parent]) == len(g[v]):
                ans = 2
        return ans
