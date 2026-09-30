"""
1293. Shortest Path in a Grid with Obstacles Elimination
Difficulty: Hard
https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

──────────────────────────────────────────────────

You are given an m x n integer matrix grid where each cell is either
0 (empty) or 1 (obstacle). You can move up, down, left, or right from
and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner
(0, 0) to the lower right corner (m - 1, n - 1) given that you can
eliminate at most k obstacles. If it is not possible to find such walk
return -1.

 

Example 1:

Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is
6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) ->
(4,2).

Example 2:

Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such
a walk.

 

Constraints:

	• m == grid.length

	• n == grid[i].length

	• 1 <= m, n <= 40

	• 1 <= k <= m * n

	• grid[i][j] is either 0 or 1.

	• grid[0][0] == grid[m - 1][n - 1] == 0
"""

class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        from collections import deque

        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0
        k = min(k, m + n - 2)
        best = [[-1] * n for _ in range(m)]
        best[0][0] = k
        q = deque([(0, 0, k, 0)])
        while q:
            i, j, rem, d = q.popleft()
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    nrem = rem - grid[ni][nj]
                    if nrem < 0:
                        continue
                    if ni == m - 1 and nj == n - 1:
                        return d + 1
                    if nrem > best[ni][nj]:
                        best[ni][nj] = nrem
                        q.append((ni, nj, nrem, d + 1))
        return -1
