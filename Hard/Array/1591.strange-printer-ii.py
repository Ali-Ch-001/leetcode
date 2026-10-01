"""
1591. Strange Printer II
Difficulty: Hard
https://leetcode.com/problems/strange-printer-ii/

──────────────────────────────────────────────────

There is a strange printer with the following two special
requirements:

• On each turn, the printer will print a solid rectangular pattern
of a single color on the grid. This will cover up the existing colors
in the rectangle.

• Once the printer has used a color for the above operation, the
same color cannot be used again.

You are given a m x n matrix targetGrid, where targetGrid[row][col]
is the color in the position (row, col) of the grid.

Return true if it is possible to print the matrix targetGrid,
otherwise, return false.

 

Example 1:

Input: targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
Output: true

Example 2:

Input: targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
Output: true

Example 3:

Input: targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
Output: false
Explanation: It is impossible to form targetGrid because it is not
allowed to print the same color in different turns.

 

Constraints:

	• m == targetGrid.length

	• n == targetGrid[i].length

	• 1 <= m, n <= 60

	• 1 <= targetGrid[row][col] <= 60
"""

class Solution:
    def isPrintable(self, targetGrid: list[list[int]]) -> bool:
        from collections import deque

        m, n = len(targetGrid), len(targetGrid[0])
        bounds = {}
        for i in range(m):
            for j in range(n):
                c = targetGrid[i][j]
                if c not in bounds:
                    bounds[c] = [i, j, i, j]
                else:
                    b = bounds[c]
                    b[0] = min(b[0], i)
                    b[1] = min(b[1], j)
                    b[2] = max(b[2], i)
                    b[3] = max(b[3], j)
        adj = {c: set() for c in bounds}
        indeg = {c: 0 for c in bounds}
        for c, (r1, c1, r2, c2) in bounds.items():
            inside = set()
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    d = targetGrid[i][j]
                    if d != c:
                        inside.add(d)
            for d in inside:
                if d not in adj[c]:
                    adj[c].add(d)
                    indeg[d] += 1
        queue = deque(c for c in indeg if indeg[c] == 0)
        processed = 0
        while queue:
            c = queue.popleft()
            processed += 1
            for d in adj[c]:
                indeg[d] -= 1
                if indeg[d] == 0:
                    queue.append(d)
        return processed == len(bounds)
