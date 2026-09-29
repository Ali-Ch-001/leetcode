"""
892. Surface Area of 3D Shapes
Difficulty: Easy
https://leetcode.com/problems/surface-area-of-3d-shapes/

──────────────────────────────────────────────────

You are given an n x n grid where you have placed some 1 x 1 x 1
cubes. Each value v = grid[i][j] represents a tower of v cubes placed
on top of cell (i, j).

After placing these cubes, you have decided to glue any directly
adjacent cubes to each other, forming several irregular 3D shapes.

Return the total surface area of the resulting shapes.

Note: The bottom face of each shape counts toward its surface area.

 

Example 1:

Input: grid = [[1,2],[3,4]]
Output: 34

Example 2:

Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 32

Example 3:

Input: grid = [[2,2,2],[2,1,2],[2,2,2]]
Output: 46

 

Constraints:

	• n == grid.length == grid[i].length

	• 1 <= n <= 50

	• 0 <= grid[i][j] <= 50
"""

class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        n = len(grid)
        total = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    total += 2
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            total += max(0, grid[r][c] - grid[nr][nc])
                        else:
                            total += grid[r][c]
        return total
