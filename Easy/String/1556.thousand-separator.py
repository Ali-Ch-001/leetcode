"""
1556. Thousand Separator
Difficulty: Easy
https://leetcode.com/problems/thousand-separator/

──────────────────────────────────────────────────

Given an integer n, add a dot (".") as the thousands separator and
return it in string format.

 

Example 1:

Input: n = 987
Output: "987"

Example 2:

Input: n = 1234
Output: "1.234"

 

Constraints:

	• 0 <= n <= 2^31 - 1
"""

class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        if len(s) <= 3:
            return s
        parts = []
        while s:
            parts.append(s[-3:])
            s = s[:-3]
        return '.'.join(reversed(parts))
