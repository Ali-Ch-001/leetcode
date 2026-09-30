"""
1124. Longest Well-Performing Interval
Difficulty: Medium
https://leetcode.com/problems/longest-well-performing-interval/

──────────────────────────────────────────────────

We are given hours, a list of the number of hours worked per day for
a given employee.

A day is considered to be a tiring day if and only if the number of
hours worked is (strictly) greater than 8.

A well-performing interval is an interval of days for which the
number of tiring days is strictly larger than the number of non-tiring
days.

Return the length of the longest well-performing interval.

 

Example 1:

Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].

Example 2:

Input: hours = [6,6,6]
Output: 0

 

Constraints:

	• 1 <= hours.length <= 10^4

	• 0 <= hours[i] <= 16
"""

class Solution:
    def longestWPI(self, hours: list[int]) -> int:
        n = len(hours)
        prefix = [0] * (n + 1)
        for i, h in enumerate(hours):
            prefix[i + 1] = prefix[i] + (1 if h > 8 else -1)

        stack = []
        for i in range(n + 1):
            if not stack or prefix[i] < prefix[stack[-1]]:
                stack.append(i)

        answer = 0
        for j in range(n, 0, -1):
            while stack and prefix[stack[-1]] < prefix[j]:
                answer = max(answer, j - stack.pop())
            if not stack:
                break
        return answer
