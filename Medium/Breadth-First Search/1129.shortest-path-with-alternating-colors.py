"""
1129. Shortest Path with Alternating Colors
Difficulty: Medium
https://leetcode.com/problems/shortest-path-with-alternating-colors/

──────────────────────────────────────────────────

You are given an integer n, the number of nodes in a directed graph
where the nodes are labeled from 0 to n - 1. Each edge is red or blue
in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

• redEdges[i] = [ai, bi] indicates that there is a directed red edge
from node ai to node bi in the graph, and

• blueEdges[j] = [uj, vj] indicates that there is a directed blue
edge from node uj to node vj in the graph.

Return an array answer of length n, where each answer[x] is the
length of the shortest path from node 0 to node x such that the edge
colors alternate along the path, or -1 if such a path does not exist.

 

Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]

Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]

 

Constraints:

	• 1 <= n <= 100

	• 0 <= redEdges.length, blueEdges.length <= 400

	• redEdges[i].length == blueEdges[j].length == 2

	• 0 <= ai, bi, uj, vj < n
"""

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        from collections import deque
        red = [[] for _ in range(n)]
        blue = [[] for _ in range(n)]
        for u, v in redEdges:
            red[u].append(v)
        for u, v in blueEdges:
            blue[u].append(v)
        INF = float('inf')
        dist = [[INF, INF] for _ in range(n)]
        dist[0][0] = dist[0][1] = 0
        q = deque([(0, 0), (0, 1)])
        while q:
            u, c = q.popleft()
            nxt = blue[u] if c == 0 else red[u]
            for v in nxt:
                if dist[v][1 - c] == INF:
                    dist[v][1 - c] = dist[u][c] + 1
                    q.append((v, 1 - c))
        ans = []
        for i in range(n):
            d = min(dist[i])
            ans.append(-1 if d == INF else d)
        return ans

