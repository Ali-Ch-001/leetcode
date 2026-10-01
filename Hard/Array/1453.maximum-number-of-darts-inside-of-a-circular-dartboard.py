"""
1453. Maximum Number of Darts Inside of a Circular Dartboard
Difficulty: Hard
https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/

──────────────────────────────────────────────────

Alice is throwing n darts on a very large wall. You are given an
array darts where darts[i] = [xi, yi] is the position of the i^th dart
that Alice threw on the wall.

Bob knows the positions of the n darts on the wall. He wants to place
a dartboard of radius r on the wall so that the maximum number of
darts that Alice throws lie on the dartboard.

Given the integer r, return the maximum number of darts that can lie
on the dartboard.

 

Example 1:

Input: darts = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
Output: 4
Explanation: Circle dartboard with center in (0,0) and radius = 2
contain all points.

Example 2:

Input: darts = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
Output: 5
Explanation: Circle dartboard with center in (0,4) and radius = 5
contain all points except the point (7,8).

 

Constraints:

	• 1 <= darts.length <= 100

	• darts[i].length == 2

	• -10^4 <= xi, yi <= 10^4

	• All the darts are unique

	• 1 <= r <= 5000
"""

class Solution:
    def numPoints(self, darts: list[list[int]], r: int) -> int:
        import math

        pts = darts
        n = len(pts)
        best = 1
        rr = r * r
        eps = 1e-6

        def count(cx, cy):
            c = 0
            for x, y in pts:
                if (x - cx) ** 2 + (y - cy) ** 2 <= rr + eps:
                    c += 1
            return c

        for i in range(n):
            x1, y1 = pts[i]
            for j in range(i + 1, n):
                x2, y2 = pts[j]
                dx, dy = x2 - x1, y2 - y1
                d2 = dx * dx + dy * dy
                d = math.sqrt(d2)
                if d > 2 * r + eps:
                    continue
                mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                h = math.sqrt(max(0.0, rr - d2 / 4))
                ux, uy = -dy / d, dx / d
                best = max(best, count(mx + h * ux, my + h * uy), count(mx - h * ux, my - h * uy))
        return best
