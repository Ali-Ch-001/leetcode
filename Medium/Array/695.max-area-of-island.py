"""
695. Max Area of Island
Difficulty: Medium
https://leetcode.com/problems/max-area-of-island/

──────────────────────────────────────────────────

You are given an m x n binary matrix grid. An island is a group of
1's (representing land) connected 4-directionally (horizontal or
vertical.) You may assume all four edges of the grid are surrounded by
water.

The area of an island is the number of cells with a value 1 in the
island.

Return the maximum area of an island in grid. If there is no island,
return 0.

 

Example 1:

Input: grid =
[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be
connected 4-directionally.

Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

 

Constraints:

	• m == grid.length

	• n == grid[i].length

	• 1 <= m, n <= 50

	• grid[i][j] is either 0 or 1.
"""

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        best = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1:
                    continue
                area = 0
                stack = [(r, c)]
                grid[r][c] = 0
                while stack:
                    x, y = stack.pop()
                    area += 1
                    for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                            grid[nx][ny] = 0
                            stack.append((nx, ny))
                best = max(best, area)
        return best
