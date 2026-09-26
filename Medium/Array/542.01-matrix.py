"""
542. 01 Matrix
Difficulty: Medium
https://leetcode.com/problems/01-matrix/

──────────────────────────────────────────────────

Given an m x n binary matrix mat, return the distance of the nearest
0 for each cell.

The distance between two cells sharing a common edge is 1.

 

Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

 

Constraints:

	• m == mat.length

	• n == mat[i].length

	• 1 <= m, n <= 10^4

	• 1 <= m * n <= 10^4

	• mat[i][j] is either 0 or 1.

	• There is at least one 0 in mat.

 

Note: This question is the same as 1765:
https://leetcode.com/problems/map-of-highest-peak/
"""

from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows, cols = len(mat), len(mat[0])
        distances = [[-1] * cols for _ in range(rows)]
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    distances[r][c] = 0
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and distances[nr][nc] == -1:
                    distances[nr][nc] = distances[r][c] + 1
                    queue.append((nr, nc))
        return distances
