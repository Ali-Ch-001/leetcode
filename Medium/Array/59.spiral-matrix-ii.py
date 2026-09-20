"""
59. Spiral Matrix II
Difficulty: Medium
https://leetcode.com/problems/spiral-matrix-ii/

──────────────────────────────────────────────────

Given a positive integer n, generate an n x n matrix filled with
elements from 1 to n^2 in spiral order.

 

Example 1:

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:

Input: n = 1
Output: [[1]]

 

Constraints:

	• 1 <= n <= 20
"""

class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        value = 1
        while top <= bottom and left <= right:
            for c in range(left, right + 1):
                matrix[top][c] = value
                value += 1
            top += 1
            for r in range(top, bottom + 1):
                matrix[r][right] = value
                value += 1
            right -= 1
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    matrix[bottom][c] = value
                    value += 1
                bottom -= 1
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    matrix[r][left] = value
                    value += 1
                left += 1
        return matrix
