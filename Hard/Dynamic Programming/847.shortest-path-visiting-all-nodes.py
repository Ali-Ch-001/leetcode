"""
847. Shortest Path Visiting All Nodes
Difficulty: Hard
https://leetcode.com/problems/shortest-path-visiting-all-nodes/

──────────────────────────────────────────────────

You have an undirected, connected graph of n nodes labeled from 0 to
n - 1. You are given an array graph where graph[i] is a list of all
the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You
may start and stop at any node, you may revisit nodes multiple times,
and you may reuse edges.

 

Example 1:

Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]

Example 2:

Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]

 

Constraints:

	• n == graph.length

	• 1 <= n <= 12

	• 0 <= graph[i].length < n

	• graph[i] does not contain i.

	• If graph[a] contains b, then graph[b] contains a.

	• The input graph is always connected.
"""

from collections import deque


class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)
        full = (1 << n) - 1
        queue = deque()
        visited = set()
        for start in range(n):
            queue.append((1 << start, start, 0))
            visited.add((1 << start, start))
        while queue:
            mask, node, distance = queue.popleft()
            if mask == full:
                return distance
            for neighbor in graph[node]:
                next_mask = mask | (1 << neighbor)
                state = (next_mask, neighbor)
                if state not in visited:
                    visited.add(state)
                    queue.append((next_mask, neighbor, distance + 1))
        return 0
