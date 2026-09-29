"""
1012. Numbers With Repeated Digits
Difficulty: Hard
https://leetcode.com/problems/numbers-with-repeated-digits/

──────────────────────────────────────────────────

Given an integer n, return the number of positive integers in the
range [1, n] that have at least one repeated digit.

 

Example 1:

Input: n = 20
Output: 1
Explanation: The only positive number (<= 20) with at least 1
repeated digit is 11.

Example 2:

Input: n = 100
Output: 10
Explanation: The positive numbers (<= 100) with atleast 1 repeated
digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.

Example 3:

Input: n = 1000
Output: 262

 

Constraints:

	• 1 <= n <= 10^9
"""

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        text = str(n)
        length = len(text)

        def perm(available, choose):
            result = 1
            for i in range(choose):
                result *= available - i
            return result

        unique = 0
        for size in range(1, length):
            unique += 9 * perm(9, size - 1)
        used = set()
        for i, ch in enumerate(text):
            digit = int(ch)
            for candidate in range(0 if i > 0 else 1, digit):
                if candidate in used:
                    continue
                unique += perm(9 - i, length - i - 1)
            if digit in used:
                break
            used.add(digit)
        else:
            unique += 1
        return n - unique
