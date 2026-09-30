"""
1154. Day of the Year
Difficulty: Easy
https://leetcode.com/problems/day-of-the-year/

──────────────────────────────────────────────────

Given a string date representing a Gregorian calendar date formatted
as YYYY-MM-DD, return the day number of the year.

 

Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.

Example 2:

Input: date = "2019-02-10"
Output: 41

 

Constraints:

	• date.length == 10

	• date[4] == date[7] == '-', and all other date[i]'s are digits

• date represents a calendar date between Jan 1^st, 1900 and Dec
31^st, 2019.
"""

class Solution:
    def dayOfYear(self, date: str) -> int:
        y, m, d = int(date[:4]), int(date[5:7]), int(date[8:])
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
            days[2] = 29
        return sum(days[:m]) + d

