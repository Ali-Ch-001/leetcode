"""
85. Maximal Rectangle
Difficulty: Hard
https://leetcode.com/problems/maximal-rectangle/

──────────────────────────────────────────────────

Given a rows x cols binary matrix filled with 0's and 1's, find the
largest rectangle containing only 1's and return its area.

 

Example 1:

Input: matrix =
[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:

Input: matrix = [["0"]]
Output: 0

Example 3:

Input: matrix = [["1"]]
Output: 1

 

Constraints:

	• rows == matrix.length

	• cols == matrix[i].length

	• 1 <= rows, cols <= 200

	• matrix[i][j] is '0' or '1'.
"""

class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0
        cols = len(matrix[0])
        heights = [0] * cols
        best = 0
        for row in matrix:
            for c in range(cols):
                heights[c] = heights[c] + 1 if row[c] == "1" else 0
            stack = []
            for i, height in enumerate(heights):
                start = i
                while stack and stack[-1][1] > height:
                    index, h = stack.pop()
                    best = max(best, h * (i - index))
                    start = index
                stack.append((start, height))
            for index, h in stack:
                best = max(best, h * (cols - index))
        return best
