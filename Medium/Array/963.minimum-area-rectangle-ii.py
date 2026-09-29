"""
963. Minimum Area Rectangle II
Difficulty: Medium
https://leetcode.com/problems/minimum-area-rectangle-ii/

──────────────────────────────────────────────────

You are given an array of points in the X-Y plane points where
points[i] = [xi, yi].

Return the minimum area of any rectangle formed from these points,
with sides not necessarily parallel to the X and Y axes. If there is
not any such rectangle, return 0.

Answers within 10^-5 of the actual answer will be accepted.

 

Example 1:

Input: points = [[1,2],[2,1],[1,0],[0,1]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at
[1,2],[2,1],[1,0],[0,1], with an area of 2.

Example 2:

Input: points = [[0,1],[2,1],[1,1],[1,0],[2,0]]
Output: 1.00000
Explanation: The minimum area rectangle occurs at
[1,0],[1,1],[2,1],[2,0], with an area of 1.

Example 3:

Input: points = [[0,3],[1,2],[3,1],[1,3],[2,1]]
Output: 0
Explanation: There is no possible rectangle to form from these points.

 

Constraints:

	• 1 <= points.length <= 50

	• points[i].length == 2

	• 0 <= xi, yi <= 4 * 10^4

	• All the given points are unique.
"""

import math
from collections import defaultdict


class Solution:
    def minAreaFreeRect(self, points: list[list[int]]) -> float:
        n = len(points)
        groups = defaultdict(list)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                center = ((x1 + x2) / 2, (y1 + y2) / 2)
                distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
                groups[(center, distance)].append((x1, y1, x2, y2))
        best = float("inf")
        for group in groups.values():
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    x1, y1, _, _ = group[i]
                    x3, y3, x4, y4 = group[j]
                    side1 = (x1 - x3) ** 2 + (y1 - y3) ** 2
                    side2 = (x1 - x4) ** 2 + (y1 - y4) ** 2
                    area = math.sqrt(side1) * math.sqrt(side2)
                    if area > 0:
                        best = min(best, area)
        return best if best != float("inf") else 0
