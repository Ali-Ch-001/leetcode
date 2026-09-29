"""
1017. Convert to Base -2
Difficulty: Medium
https://leetcode.com/problems/convert-to-base-2/

──────────────────────────────────────────────────

Given an integer n, return a binary string representing its
representation in base -2.

Note that the returned string should not have leading zeros unless
the string is "0".

 

Example 1:

Input: n = 2
Output: "110"
Explantion: (-2)^2 + (-2)^1 = 2

Example 2:

Input: n = 3
Output: "111"
Explantion: (-2)^2 + (-2)^1 + (-2)^0 = 3

Example 3:

Input: n = 4
Output: "100"
Explantion: (-2)^2 = 4

 

Constraints:

	• 0 <= n <= 10^9
"""

class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        result = []
        while n:
            remainder = n % -2
            n //= -2
            if remainder < 0:
                remainder += 2
                n += 1
            result.append(str(remainder))
        return "".join(reversed(result))
