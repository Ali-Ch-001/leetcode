"""
827. Making A Large Island
Difficulty: Hard
https://leetcode.com/problems/making-a-large-island/

──────────────────────────────────────────────────

You are given an n x n binary matrix grid. You are allowed to change
at most one 0 to be 1.

Return the size of the largest island in grid after applying this
operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an
island with area = 3.

Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one
island with area = 4.

Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

 

Constraints:

	• n == grid.length

	• n == grid[i].length

	• 1 <= n <= 500

	• grid[i][j] is either 0 or 1.
"""

class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        island_id = 2
        sizes = {}

        def explore(r, c, island):
            stack = [(r, c)]
            grid[r][c] = island
            size = 0
            while stack:
                x, y = stack.pop()
                size += 1
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = island
                        stack.append((nx, ny))
            return size

        best = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    sizes[island_id] = explore(r, c, island_id)
                    best = max(best, sizes[island_id])
                    island_id += 1
        if not sizes:
            return 1
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    neighbors = set()
                    for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] >= 2:
                            neighbors.add(grid[nr][nc])
                    candidate = 1 + sum(sizes[i] for i in neighbors)
                    best = max(best, candidate)
        return best
