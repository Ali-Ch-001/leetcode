"""
149. Max Points on a Line
Difficulty: Hard
https://leetcode.com/problems/max-points-on-a-line/

──────────────────────────────────────────────────

Given an array of points where points[i] = [xi, yi] represents a
point on the X-Y plane, return the maximum number of points that lie
on the same straight line.

 

Example 1:

Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:

Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

 

Constraints:

	• 1 <= points.length <= 300

	• points[i].length == 2

	• -10^4 <= xi, yi <= 10^4

	• All the points are unique.
"""

import math


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        best = 2
        for i in range(len(points)):
            slopes = {}
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dx, dy = x2 - x1, y2 - y1
                if dx == 0:
                    key = (0, 1)
                elif dy == 0:
                    key = (1, 0)
                else:
                    g = math.gcd(abs(dx), abs(dy))
                    dx //= g
                    dy //= g
                    if dx < 0:
                        dx, dy = -dx, -dy
                    key = (dx, dy)
                slopes[key] = slopes.get(key, 0) + 1
                best = max(best, slopes[key] + 1)
        return best
