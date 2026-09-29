"""
931. Minimum Falling Path Sum
Difficulty: Medium
https://leetcode.com/problems/minimum-falling-path-sum/

──────────────────────────────────────────────────

Given an n x n array of integers matrix, return the minimum sum of
any falling path through matrix.

A falling path starts at any element in the first row and chooses the
element in the next row that is either directly below or diagonally
left/right. Specifically, the next element from position (row, col)
will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 

Example 1:

Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.

Example 2:

Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.

 

Constraints:

	• n == matrix.length == matrix[i].length

	• 1 <= n <= 100

	• -100 <= matrix[i][j] <= 100
"""

class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        row = matrix[0][:]
        for r in range(1, n):
            new_row = [0] * n
            for c in range(n):
                best = row[c]
                if c > 0:
                    best = min(best, row[c - 1])
                if c < n - 1:
                    best = min(best, row[c + 1])
                new_row[c] = matrix[r][c] + best
            row = new_row
        return min(row)
