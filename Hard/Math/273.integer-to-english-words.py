"""
273. Integer to English Words
Difficulty: Hard
https://leetcode.com/problems/integer-to-english-words/

──────────────────────────────────────────────────

Convert a non-negative integer num to its English words
representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred
Sixty Seven"

 

Constraints:

	• 0 <= num <= 2^31 - 1
"""

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
                "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        def under_thousand(value: int) -> str:
            if value == 0:
                return ""
            if value < 20:
                return ones[value]
            if value < 100:
                return (tens[value // 10] + " " + ones[value % 10]).strip()
            return (ones[value // 100] + " Hundred " + under_thousand(value % 100)).strip()

        parts = []
        for divisor, name in ((10**9, "Billion"), (10**6, "Million"), (10**3, "Thousand")):
            if num >= divisor:
                parts.append(under_thousand(num // divisor) + " " + name)
                num %= divisor
        remaining = under_thousand(num)
        if remaining:
            parts.append(remaining)
        return " ".join(parts)
