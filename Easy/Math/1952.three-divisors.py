"""
1952. Three Divisors
Difficulty: Easy
https://leetcode.com/problems/three-divisors/

──────────────────────────────────────────────────

Given an integer n, return true if n has exactly three positive
divisors. Otherwise, return false.

An integer m is a divisor of n if there exists an integer k such that
n = k * m.

 

Example 1:

Input: n = 2
Output: false
Explantion: 2 has only two divisors: 1 and 2.

Example 2:

Input: n = 4
Output: true
Explantion: 4 has three divisors: 1, 2, and 4.

 

Constraints:

	• 1 <= n <= 10^4
"""

class Solution:
    def isThree(self, n: int) -> bool:
        cnt = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                cnt += 1 if i * i == n else 2
            i += 1
        return cnt == 3

