"""
1254. Number of Closed Islands
Difficulty: Medium
https://leetcode.com/problems/number-of-closed-islands/

──────────────────────────────────────────────────

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a
maximal 4-directionally connected group of 0s and a closed island is
an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:

Input: grid =
[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by
water (group of 1s).

Example 2:

Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2

 

Constraints:

	• 1 <= grid.length, grid[0].length <= 100

	• 0 <= grid[i][j] <=1
"""

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    continue
                stack = [(i, j)]
                grid[i][j] = 1
                closed = True
                while stack:
                    x, y = stack.pop()
                    if x == 0 or y == 0 or x == m - 1 or y == n - 1:
                        closed = False
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                            grid[nx][ny] = 1
                            stack.append((nx, ny))
                if closed:
                    count += 1
        return count
