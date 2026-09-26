"""
498. Diagonal Traverse
Difficulty: Medium
https://leetcode.com/problems/diagonal-traverse/

──────────────────────────────────────────────────

Given an m x n matrix mat, return an array of all the elements of the
array in a diagonal order.

 

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

 

Constraints:

	• m == mat.length

	• n == mat[i].length

	• 1 <= m, n <= 10^4

	• 1 <= m * n <= 10^4

	• -10^5 <= mat[i][j] <= 10^5
"""

class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        rows, cols = len(mat), len(mat[0])
        result = []
        for diagonal in range(rows + cols - 1):
            if diagonal % 2 == 0:
                r = min(diagonal, rows - 1)
                c = diagonal - r
                while r >= 0 and c < cols:
                    result.append(mat[r][c])
                    r -= 1
                    c += 1
            else:
                c = min(diagonal, cols - 1)
                r = diagonal - c
                while c >= 0 and r < rows:
                    result.append(mat[r][c])
                    r += 1
                    c -= 1
        return result
