"""
1579. Remove Max Number of Edges to Keep Graph Fully Traversable
Difficulty: Hard
https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

──────────────────────────────────────────────────

Alice and Bob have an undirected graph of n nodes and three types of
edges:

	• Type 1: Can be traversed by Alice only.

	• Type 2: Can be traversed by Bob only.

	• Type 3: Can be traversed by both Alice and Bob.

Given an array edges where edges[i] = [typei, ui, vi] represents a
bidirectional edge of type typei between nodes ui and vi, find the
maximum number of edges you can remove so that after removing the
edges, the graph can still be fully traversed by both Alice and Bob.
The graph is fully traversed by Alice and Bob if starting from any
node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if
Alice and Bob cannot fully traverse the graph.

 

Example 1:

Input: n = 4, edges =
[[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph
will still be fully traversable by Alice and Bob. Removing any
additional edge will not make it so. So the maximum number of edges we
can remove is 2.

Example 2:

Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph
fully traversable by Alice and Bob.

Example 3:

Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the
other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible
to make the graph fully traversable.

 

 

Constraints:

	• 1 <= n <= 10^5

	• 1 <= edges.length <= min(10^5, 3 * n * (n - 1) / 2)

	• edges[i].length == 3

	• 1 <= typei <= 3

	• 1 <= ui < vi <= n

	• All tuples (typei, ui, vi) are distinct.
"""

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        parent_a = list(range(n + 1))
        parent_b = list(range(n + 1))

        def find(parent: list[int], x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(parent: list[int], a: int, b: int) -> bool:
            ra, rb = find(parent, a), find(parent, b)
            if ra == rb:
                return False
            parent[ra] = rb
            return True

        ans = 0
        for t, u, v in edges:
            if t == 3:
                used_a = union(parent_a, u, v)
                used_b = union(parent_b, u, v)
                if not used_a and not used_b:
                    ans += 1
        for t, u, v in edges:
            if t == 1:
                if not union(parent_a, u, v):
                    ans += 1
            elif t == 2:
                if not union(parent_b, u, v):
                    ans += 1
        for parent in (parent_a, parent_b):
            root = find(parent, 1)
            for node in range(2, n + 1):
                if find(parent, node) != root:
                    return -1
        return ans
