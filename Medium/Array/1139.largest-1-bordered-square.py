"""
1139. Largest 1-Bordered Square
Difficulty: Medium
https://leetcode.com/problems/largest-1-bordered-square/

──────────────────────────────────────────────────

Given a 2D grid of 0s and 1s, return the number of elements in the
largest square subgrid that has all 1s on its border, or 0 if such a
subgrid doesn't exist in the grid.



 



Example 1:




Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 9



Example 2:




Input: grid = [[1,1,0,0]]
Output: 1


 


Constraints:




	• 1 <= grid.length <= 100

	• 1 <= grid[0].length <= 100

	• grid[i][j] is 0 or 1
"""

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        right = [[0] * (n + 1) for _ in range(m + 1)]
        down = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j]:
                    right[i][j] = right[i][j + 1] + 1
                    down[i][j] = down[i + 1][j] + 1
        best = 0
        for i in range(m):
            for j in range(n):
                for k in range(min(m - i, n - j), best, -1):
                    if (right[i][j] >= k and down[i][j] >= k
                            and right[i + k - 1][j] >= k
                            and down[i][j + k - 1] >= k):
                        best = k
                        break
        return best * best

