"""
1034. Coloring A Border
Difficulty: Medium
https://leetcode.com/problems/coloring-a-border/

──────────────────────────────────────────────────

You are given an m x n integer matrix grid, and three integers row,
col, and color. Each value in the grid represents the color of the
grid square at that location.

Two squares are called adjacent if they are next to each other in any
of the 4 directions.

Two squares belong to the same connected component if they have the
same color and they are adjacent.

The border of a connected component is all the squares in the
connected component that are either adjacent to (at least) a square
not in the component, or on the boundary of the grid (the first or
last row or column).

You should color the border of the connected component that contains
the square grid[row][col] with color.

Return the final grid.

 

Example 1:

Input: grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
Output: [[3,3],[3,2]]

Example 2:

Input: grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
Output: [[1,3,3],[2,3,3]]

Example 3:

Input: grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
Output: [[2,2,2],[2,1,2],[2,2,2]]

 

Constraints:

	• m == grid.length

	• n == grid[i].length

	• 1 <= m, n <= 50

	• 1 <= grid[i][j], color <= 1000

	• 0 <= row < m

	• 0 <= col < n
"""

class Solution:
    def colorBorder(self, grid: list[list[int]], row: int, col: int, color: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        orig = grid[row][col]
        comp = {(row, col)}
        stack = [(row, col)]
        while stack:
            r, c = stack.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in comp and grid[nr][nc] == orig:
                    comp.add((nr, nc))
                    stack.append((nr, nc))
        border = []
        for r, c in comp:
            if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                border.append((r, c))
            else:
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    if (r + dr, c + dc) not in comp:
                        border.append((r, c))
                        break
        for r, c in border:
            grid[r][c] = color
        return grid
