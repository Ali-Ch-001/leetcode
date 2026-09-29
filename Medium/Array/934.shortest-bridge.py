"""
934. Shortest Bridge
Difficulty: Medium
https://leetcode.com/problems/shortest-bridge/

──────────────────────────────────────────────────

You are given an n x n binary matrix grid where 1 represents land and
0 represents water.

An island is a 4-directionally connected group of 1's not connected
to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one
island.

Return the smallest number of 0's you must flip to connect the two
islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1

Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:

Input: grid =
[[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

 

Constraints:

	• n == grid.length == grid[i].length

	• 2 <= n <= 100

	• grid[i][j] is either 0 or 1.

	• There are exactly two islands in grid.
"""

from collections import deque


class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        n = len(grid)
        first_island = []
        found = False
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    stack = [(r, c)]
                    grid[r][c] = 2
                    while stack:
                        x, y = stack.pop()
                        first_island.append((x, y))
                        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                                grid[nx][ny] = 2
                                stack.append((nx, ny))
                    found = True
                    break
            if found:
                break
        queue = deque((x, y, 0) for x, y in first_island)
        while queue:
            x, y, distance = queue.popleft()
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= nx < n and 0 <= ny < n:
                    if grid[nx][ny] == 1:
                        return distance
                    if grid[nx][ny] == 0:
                        grid[nx][ny] = 2
                        queue.append((nx, ny, distance + 1))
        return -1
