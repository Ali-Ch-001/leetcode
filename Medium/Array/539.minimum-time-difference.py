"""
539. Minimum Time Difference
Difficulty: Medium
https://leetcode.com/problems/minimum-time-difference/

──────────────────────────────────────────────────

Given a list of 24-hour clock time points in "HH:MM" format, return
the minimum minutes difference between any two time-points in the
list.
 

Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1

Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0

 

Constraints:

	• 2 <= timePoints.length <= 2 * 10^4

	• timePoints[i] is in the format "HH:MM".
"""

class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        minutes = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
        best = 24 * 60 - minutes[-1] + minutes[0]
        for i in range(1, len(minutes)):
            best = min(best, minutes[i] - minutes[i - 1])
        return best
