"""
1895. Largest Magic Square
Difficulty: Medium
https://leetcode.com/problems/largest-magic-square/

──────────────────────────────────────────────────

A k x k magic square is a k x k grid filled with integers such that
every row sum, every column sum, and both diagonal sums are all equal.
The integers in the magic square do not have to be distinct. Every 1 x
1 grid is trivially a magic square.

Given an m x n integer grid, return the size (i.e., the side length
k) of the largest magic square that can be found within this grid.

 

Example 1:

Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
Output: 3
Explanation: The largest magic square has a size of 3.
Every row sum, column sum, and diagonal sum of this magic square is
equal to 12.
- Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
- Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
- Diagonal sums: 5+4+3 = 6+4+2 = 12

Example 2:

Input: grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
Output: 2

 

Constraints:

	• m == grid.length

	• n == grid[i].length

	• 1 <= m, n <= 50

	• 1 <= grid[i][j] <= 10^6
"""

class Solution:
    def largestMagicSquare(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = [[0] * (n + 1) for _ in range(m)]
        cols = [[0] * (m + 1) for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rows[i][j + 1] = rows[i][j] + grid[i][j]
                cols[j][i + 1] = cols[j][i] + grid[i][j]
        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    target = rows[i][j + k] - rows[i][j]
                    if any(
                        rows[i + r][j + k] - rows[i + r][j] != target
                        for r in range(1, k)
                    ):
                        continue
                    if any(
                        cols[j + c][i + k] - cols[j + c][i] != target
                        for c in range(1, k)
                    ):
                        continue
                    d1 = sum(grid[i + d][j + d] for d in range(k))
                    d2 = sum(grid[i + d][j + k - 1 - d] for d in range(k))
                    if d1 == target and d2 == target:
                        return k
        return 1
