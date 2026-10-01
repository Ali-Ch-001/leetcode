"""
1568. Minimum Number of Days to Disconnect Island
Difficulty: Hard
https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/

──────────────────────────────────────────────────

You are given an m x n binary grid grid where 1 represents land and 0
represents water. An island is a maximal 4-directionally (horizontal
or vertical) connected group of 1's.

The grid is said to be connected if we have exactly one island,
otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1) into a
water cell (0).

Return the minimum number of days to disconnect the grid.

 

Example 1:

Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]

Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 disconnected
island.

Example 2:

Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] ->
[[0,0]]), 0 islands.

 

Constraints:

	• m == grid.length

	• n == grid[i].length

	• 1 <= m, n <= 30

	• grid[i][j] is either 0 or 1.
"""

class Solution:
    def minDays(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def count_islands(g):
            seen = [[False] * n for _ in range(m)]
            c = 0
            for i in range(m):
                for j in range(n):
                    if g[i][j] == 1 and not seen[i][j]:
                        c += 1
                        if c > 1:
                            return c
                        seen[i][j] = True
                        stack = [(i, j)]
                        while stack:
                            x, y = stack.pop()
                            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < m and 0 <= ny < n and g[nx][ny] == 1 and not seen[nx][ny]:
                                    seen[nx][ny] = True
                                    stack.append((nx, ny))
            return c
        if count_islands(grid) != 1:
            return 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands(grid) != 1:
                        grid[i][j] = 1
                        return 1
                    grid[i][j] = 1
        return 2
