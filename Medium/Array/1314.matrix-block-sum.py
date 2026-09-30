"""
1314. Matrix Block Sum
Difficulty: Medium
https://leetcode.com/problems/matrix-block-sum/

──────────────────────────────────────────────────

Given a m x n matrix mat and an integer k, return a matrix answer
where each answer[i][j] is the sum of all elements mat[r][c] for:

	• i - k <= r <= i + k,

	• j - k <= c <= j + k, and

	• (r, c) is a valid position in the matrix.

 

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]

Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]

 

Constraints:

	• m == mat.length

	• n == mat[i].length

	• 1 <= m, n, k <= 100

	• 1 <= mat[i][j] <= 100
"""

class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (prefix[i][j + 1] + prefix[i + 1][j]
                                        - prefix[i][j] + mat[i][j])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            r1, r2 = max(0, i - k), min(m - 1, i + k)
            for j in range(n):
                c1, c2 = max(0, j - k), min(n - 1, j + k)
                ans[i][j] = (prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1]
                             - prefix[r2 + 1][c1] + prefix[r1][c1])
        return ans
