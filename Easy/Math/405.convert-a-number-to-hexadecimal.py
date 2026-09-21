"""
405. Convert a Number to Hexadecimal
Difficulty: Easy
https://leetcode.com/problems/convert-a-number-to-hexadecimal/

──────────────────────────────────────────────────

Given a 32-bit integer num, return a string representing its
hexadecimal representation. For negative integers, two&rsquo;s
complement method is used.

All the letters in the answer string should be lowercase characters,
and there should not be any leading zeros in the answer except for the
zero itself.

Note: You are not allowed to use any built-in library method to
directly solve this problem.

 

Example 1:

Input: num = 26
Output: "1a"

Example 2:

Input: num = -1
Output: "ffffffff"

 

Constraints:

	• -2^31 <= num <= 2^31 - 1
"""

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        digits = "0123456789abcdef"
        num &= 0xFFFFFFFF
        result = []
        while num:
            result.append(digits[num & 0xF])
            num >>= 4
        return "".join(reversed(result))
