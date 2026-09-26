"""
504. Base 7
Difficulty: Easy
https://leetcode.com/problems/base-7/

──────────────────────────────────────────────────

Given an integer num, return a string of its base 7 representation.

 

Example 1:

Input: num = 100
Output: "202"

Example 2:

Input: num = -7
Output: "-10"

 

Constraints:

	• -10^7 <= num <= 10^7
"""

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        negative = num < 0
        num = abs(num)
        digits = []
        while num:
            digits.append(str(num % 7))
            num //= 7
        result = "".join(reversed(digits))
        return "-" + result if negative else result
