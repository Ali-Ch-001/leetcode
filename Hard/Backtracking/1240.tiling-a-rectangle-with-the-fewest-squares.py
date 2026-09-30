"""
1240. Tiling a Rectangle with the Fewest Squares
Difficulty: Hard
https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

──────────────────────────────────────────────────

Given a rectangle of size n x m, return the minimum number of
integer-sided squares that tile the rectangle.

 

Example 1:

Input: n = 2, m = 3
Output: 3
Explanation: 3 squares are necessary to cover the rectangle.
2 (squares of 1x1)
1 (square of 2x2)

Example 2:

Input: n = 5, m = 8
Output: 5

Example 3:

Input: n = 11, m = 13
Output: 6

 

Constraints:

	• 1 <= n, m <= 13
"""

class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n == m:
            return 1
        if n > m:
            n, m = m, n
        best = n * m
        h = [0] * n

        def dfs(cnt):
            nonlocal best
            if cnt >= best:
                return
            i = min(range(n), key=lambda k: h[k])
            if h[i] == m:
                best = cnt
                return
            max_w = min(m - h[i], n - i)
            j = i
            while j < n and h[j] == h[i]:
                j += 1
            max_w = min(max_w, j - i)
            for w in range(max_w, 0, -1):
                for k in range(i, i + w):
                    h[k] += w
                dfs(cnt + 1)
                for k in range(i, i + w):
                    h[k] -= w

        dfs(0)
        return best
