"""
878. Nth Magical Number
Difficulty: Hard
https://leetcode.com/problems/nth-magical-number/

──────────────────────────────────────────────────

A positive integer is magical if it is divisible by either a or b.

Given the three integers n, a, and b, return the n^th magical number.
Since the answer may be very large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1, a = 2, b = 3
Output: 2

Example 2:

Input: n = 4, a = 2, b = 3
Output: 6

 

Constraints:

	• 1 <= n <= 10^9

	• 2 <= a, b <= 4 * 10^4
"""

import math


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7
        lcm = a * b // math.gcd(a, b)
        lo, hi = 1, n * min(a, b)
        while lo < hi:
            mid = (lo + hi) // 2
            count = mid // a + mid // b - mid // lcm
            if count >= n:
                hi = mid
            else:
                lo = mid + 1
        return lo % MOD
