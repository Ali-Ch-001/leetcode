"""
1931. Painting a Grid With Three Different Colors
Difficulty: Hard
https://leetcode.com/problems/painting-a-grid-with-three-different-colors/

──────────────────────────────────────────────────

You are given two integers m and n. Consider an m x n grid where each
cell is initially white. You can paint each cell red, green, or blue.
All cells must be painted.

Return the number of ways to color the grid with no two adjacent
cells having the same color. Since the answer can be very large,
return it modulo 10^9 + 7.

 

Example 1:

Input: m = 1, n = 1
Output: 3
Explanation: The three possible colorings are shown in the image
above.

Example 2:

Input: m = 1, n = 2
Output: 6
Explanation: The six possible colorings are shown in the image above.

Example 3:

Input: m = 5, n = 5
Output: 580986

 

Constraints:

	• 1 <= m <= 5

	• 1 <= n <= 1000
"""

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        patterns = []
        for mask in range(3 ** m):
            p = []
            x = mask
            for _ in range(m):
                p.append(x % 3)
                x //= 3
            if all(p[i] != p[i + 1] for i in range(m - 1)):
                patterns.append(tuple(p))
        k = len(patterns)
        compat = [[] for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if all(patterns[i][r] != patterns[j][r] for r in range(m)):
                    compat[i].append(j)
        dp = [1] * k
        for _ in range(n - 1):
            ndp = [0] * k
            for i in range(k):
                total = 0
                for j in compat[i]:
                    total += dp[j]
                ndp[i] = total % MOD
            dp = ndp
        return sum(dp) % MOD
