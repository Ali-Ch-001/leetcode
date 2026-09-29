"""
939. Minimum Area Rectangle
Difficulty: Medium
https://leetcode.com/problems/minimum-area-rectangle/

──────────────────────────────────────────────────

You are given an array of points in the X-Y plane points where
points[i] = [xi, yi].

Return the minimum area of a rectangle formed from these points, with
sides parallel to the X and Y axes. If there is not any such
rectangle, return 0.

 

Example 1:

Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4

Example 2:

Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2

 

Constraints:

	• 1 <= points.length <= 500

	• points[i].length == 2

	• 0 <= xi, yi <= 4 * 10^4

	• All the given points are unique.
"""

class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        point_set = {tuple(point) for point in points}
        best = float("inf")
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        best = min(best, abs(x2 - x1) * abs(y2 - y1))
        return best if best != float("inf") else 0
