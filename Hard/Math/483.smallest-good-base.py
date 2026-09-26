"""
483. Smallest Good Base
Difficulty: Hard
https://leetcode.com/problems/smallest-good-base/

──────────────────────────────────────────────────

Given an integer n represented as a string, return the smallest good
base of n.

We call k >= 2 a good base of n, if all digits of n base k are 1's.

 

Example 1:

Input: n = "13"
Output: "3"
Explanation: 13 base 3 is 111.

Example 2:

Input: n = "4681"
Output: "8"
Explanation: 4681 base 8 is 11111.

Example 3:

Input: n = "1000000000000000000"
Output: "999999999999999999"
Explanation: 1000000000000000000 base 999999999999999999 is 11.

 

Constraints:

	• n is an integer in the range [3, 10^18].

	• n does not contain any leading zeros.
"""

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        value = int(n)
        for length in range(len(bin(value)) - 2, 1, -1):
            base = int(value ** (1 / (length - 1)))
            if base > 1 and sum(base ** i for i in range(length)) == value:
                return str(base)
        return str(value - 1)
