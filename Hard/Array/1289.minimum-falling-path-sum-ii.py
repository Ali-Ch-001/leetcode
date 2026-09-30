"""
1289. Minimum Falling Path Sum II
Difficulty: Hard
https://leetcode.com/problems/minimum-falling-path-sum-ii/

──────────────────────────────────────────────────

Given an n x n integer matrix grid, return the minimum sum of a
falling path with non-zero shifts.

A falling path with non-zero shifts is a choice of exactly one
element from each row of grid such that no two elements chosen in
adjacent rows are in the same column.

 

Example 1:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: 13
Explanation: 
The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is [1,5,7], so the answer is
13.

Example 2:

Input: grid = [[7]]
Output: 7

 

Constraints:

	• n == grid.length == grid[i].length

	• 1 <= n <= 200

	• -99 <= grid[i][j] <= 99
"""

class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dp = list(grid[0])
        for i in range(1, n):
            best1 = best2 = float('inf')
            idx1 = -1
            for j, v in enumerate(dp):
                if v < best1:
                    best2 = best1
                    best1 = v
                    idx1 = j
                elif v < best2:
                    best2 = v
            ndp = [0] * n
            for j in range(n):
                ndp[j] = grid[i][j] + (best2 if j == idx1 else best1)
            dp = ndp
        return min(dp)
