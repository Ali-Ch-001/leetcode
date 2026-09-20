"""
64. Minimum Path Sum
Difficulty: Medium
https://leetcode.com/problems/minimum-path-sum/

──────────────────────────────────────────────────

Given a m x n grid filled with non-negative numbers, find a path from
top left to bottom right, which minimizes the sum of all numbers along
its path.

Note: You can only move either down or right at any point in time.

 

Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 &rarr; 3 &rarr; 1 &rarr; 1 &rarr; 1
minimizes the sum.

Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12

 

Constraints:

	• m == grid.length

	• n == grid[i].length

	• 1 <= m, n <= 200

	• 0 <= grid[i][j] <= 200
"""

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        dp = [0] * n
        for r, row in enumerate(grid):
            for c in range(n):
                if r == 0 and c == 0:
                    dp[c] = row[c]
                elif r == 0:
                    dp[c] = dp[c - 1] + row[c]
                elif c == 0:
                    dp[c] += row[c]
                else:
                    dp[c] = min(dp[c], dp[c - 1]) + row[c]
        return dp[-1]
