"""
329. Longest Increasing Path in a Matrix
Difficulty: Hard
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

──────────────────────────────────────────────────

Given an m x n integers matrix, return the length of the longest
increasing path in matrix.

From each cell, you can either move in four directions: left, right,
up, or down. You may not move diagonally or move outside the boundary
(i.e., wrap-around is not allowed).

 

Example 1:

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:

Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving
diagonally is not allowed.

Example 3:

Input: matrix = [[1]]
Output: 1

 

Constraints:

	• m == matrix.length

	• n == matrix[i].length

	• 1 <= m, n <= 200

	• 0 <= matrix[i][j] <= 2^31 - 1
"""

class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]

        def dfs(r: int, c: int) -> int:
            if memo[r][c]:
                return memo[r][c]
            best = 1
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))
            memo[r][c] = best
            return best

        return max(dfs(r, c) for r in range(rows) for c in range(cols))
