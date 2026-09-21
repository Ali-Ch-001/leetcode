"""
233. Number of Digit One
Difficulty: Hard
https://leetcode.com/problems/number-of-digit-one/

──────────────────────────────────────────────────

Given an integer n, count the total number of digit 1 appearing in
all non-negative integers less than or equal to n.

 

Example 1:

Input: n = 13
Output: 6

Example 2:

Input: n = 0
Output: 0

 

Constraints:

	• 0 <= n <= 10^9
"""

class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        factor = 1
        while factor <= n:
            higher = n // (factor * 10)
            current = (n // factor) % 10
            lower = n % factor
            if current == 0:
                count += higher * factor
            elif current == 1:
                count += higher * factor + lower + 1
            else:
                count += (higher + 1) * factor
            factor *= 10
        return count
