"""
1192. Critical Connections in a Network
Difficulty: Hard
https://leetcode.com/problems/critical-connections-in-a-network/

──────────────────────────────────────────────────

There are n servers numbered from 0 to n - 1 connected by undirected
server-to-server connections forming a network where connections[i] =
[ai, bi] represents a connection between servers ai and bi. Any server
can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make
some servers unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:

Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]

 

Constraints:

	• 2 <= n <= 10^5

	• n - 1 <= connections.length <= 10^5

	• 0 <= ai, bi <= n - 1

	• ai != bi

	• There are no repeated connections.
"""

class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        g = [[] for _ in range(n)]
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)
        disc = [-1] * n
        low = [0] * n
        res = []
        timer = 0
        for root in range(n):
            if disc[root] != -1:
                continue
            disc[root] = low[root] = timer
            timer += 1
            stack = [[root, -1, 0]]
            while stack:
                frame = stack[-1]
                u, p, idx = frame
                if idx < len(g[u]):
                    frame[2] += 1
                    v = g[u][idx]
                    if v == p:
                        continue
                    if disc[v] == -1:
                        disc[v] = low[v] = timer
                        timer += 1
                        stack.append([v, u, 0])
                    elif disc[v] < low[u]:
                        low[u] = disc[v]
                else:
                    stack.pop()
                    if stack:
                        parent = stack[-1][0]
                        if low[u] < low[parent]:
                            low[parent] = low[u]
                        if low[u] > disc[parent]:
                            res.append([parent, u])
        return res
        
