"""
1925. Count Square Sum Triples
Difficulty: Easy
https://leetcode.com/problems/count-square-sum-triples/

──────────────────────────────────────────────────

A square triple (a,b,c) is a triple where a, b, and c are integers
and a^2 + b^2 = c^2.

Given an integer n, return the number of square triples such that 1
<= a, b, c <= n.

 

Example 1:

Input: n = 5
Output: 2
Explanation: The square triples are (3,4,5) and (4,3,5).

Example 2:

Input: n = 10
Output: 4
Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and
(8,6,10).

 

Constraints:

	• 1 <= n <= 250
"""

from math import isqrt


class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for c in range(1, n + 1):
            cc = c * c
            for a in range(1, c):
                b = isqrt(cc - a * a)
                if b >= 1 and b * b == cc - a * a:
                    ans += 1
        return ans
