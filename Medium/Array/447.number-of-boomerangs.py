"""
447. Number of Boomerangs
Difficulty: Medium
https://leetcode.com/problems/number-of-boomerangs/

──────────────────────────────────────────────────

You are given n points in the plane that are all distinct, where
points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k) such
that the distance between i and j equals the distance between i and k
(the order of the tuple matters).

Return the number of boomerangs.

 

Example 1:

Input: points = [[0,0],[1,0],[2,0]]
Output: 2
Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and
[[1,0],[2,0],[0,0]].

Example 2:

Input: points = [[1,1],[2,2],[3,3]]
Output: 2

Example 3:

Input: points = [[1,1]]
Output: 0

 

Constraints:

	• n == points.length

	• 1 <= n <= 500

	• points[i].length == 2

	• -10^4 <= xi, yi <= 10^4

	• All the points are unique.
"""

class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        total = 0
        for x1, y1 in points:
            distances = {}
            for x2, y2 in points:
                d = (x1 - x2) ** 2 + (y1 - y2) ** 2
                distances[d] = distances.get(d, 0) + 1
            for count in distances.values():
                total += count * (count - 1)
        return total
