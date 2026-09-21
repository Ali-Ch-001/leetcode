"""
166. Fraction to Recurring Decimal
Difficulty: Medium
https://leetcode.com/problems/fraction-to-recurring-decimal/

──────────────────────────────────────────────────

Given two integers representing the numerator and denominator of a
fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in
parentheses

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than
10^4 for all the given inputs.

Note that if the fraction can be represented as a finite length
string, you must return it.

 

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:

Input: numerator = 2, denominator = 1
Output: "2"

Example 3:

Input: numerator = 4, denominator = 333
Output: "0.(012)"

 

Constraints:

	• -2^31 <= numerator, denominator <= 2^31 - 1

	• denominator != 0
"""

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        sign = "-" if (numerator < 0) != (denominator < 0) else ""
        numerator, denominator = abs(numerator), abs(denominator)
        integer_part, remainder = divmod(numerator, denominator)
        result = sign + str(integer_part)
        if remainder == 0:
            return result
        result += "."
        seen = {}
        digits = []
        while remainder:
            if remainder in seen:
                index = seen[remainder]
                digits.insert(index, "(")
                digits.append(")")
                break
            seen[remainder] = len(digits)
            remainder *= 10
            digit, remainder = divmod(remainder, denominator)
            digits.append(str(digit))
        return result + "".join(digits)
