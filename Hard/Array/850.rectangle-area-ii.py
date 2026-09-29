"""
850. Rectangle Area II
Difficulty: Hard
https://leetcode.com/problems/rectangle-area-ii/

──────────────────────────────────────────────────

You are given a 2D array of axis-aligned rectangles. Each
rectangle[i] = [xi1, yi1, xi2, yi2] denotes the i^th rectangle where
(xi1, yi1) are the coordinates of the bottom-left corner, and (xi2,
yi2) are the coordinates of the top-right corner.

Calculate the total area covered by all rectangles in the plane. Any
area covered by two or more rectangles should only be counted once.

Return the total area. Since the answer may be too large, return it
modulo 10^9 + 7.

 

Example 1:

Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: A total area of 6 is covered by all three rectangles, as
illustrated in the picture.
From (1,1) to (2,2), the green and red rectangles overlap.
From (1,0) to (2,3), all three rectangles overlap.

Example 2:

Input: rectangles = [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 10^18 modulo (10^9 + 7), which is 49.

 

Constraints:

	• 1 <= rectangles.length <= 200

	• rectanges[i].length == 4

	• 0 <= xi1, yi1, xi2, yi2 <= 10^9

	• xi1 <= xi2

	• yi1 <= yi2

	• All rectangles have non zero area.
"""

class Solution:
    def rectangleArea(self, rectangles: list[list[int]]) -> int:
        MOD = 10**9 + 7
        xs = sorted({x for rx1, _, rx2, _ in rectangles for x in (rx1, rx2)})
        total = 0
        for i in range(len(xs) - 1):
            x1, x2 = xs[i], xs[i + 1]
            intervals = []
            for rx1, ry1, rx2, ry2 in rectangles:
                if rx1 <= x1 and rx2 >= x2:
                    intervals.append((ry1, ry2))
            if not intervals:
                continue
            intervals.sort()
            covered = 0
            current_start, current_end = intervals[0]
            for start, end in intervals[1:]:
                if start > current_end:
                    covered += current_end - current_start
                    current_start, current_end = start, end
                else:
                    current_end = max(current_end, end)
            covered += current_end - current_start
            total += covered * (x2 - x1)
        return total % MOD
