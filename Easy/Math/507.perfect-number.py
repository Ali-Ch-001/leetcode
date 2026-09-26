"""
507. Perfect Number
Difficulty: Easy
https://leetcode.com/problems/perfect-number/

──────────────────────────────────────────────────

A perfect number is a positive integer that is equal to the sum of
its positive divisors, excluding the number itself. A divisor of an
integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise
return false.

 

Example 1:

Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.

Example 2:

Input: num = 7
Output: false

 

Constraints:

	• 1 <= num <= 10^8
"""

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        total = 1
        divisor = 2
        while divisor * divisor <= num:
            if num % divisor == 0:
                total += divisor
                if divisor != num // divisor:
                    total += num // divisor
            divisor += 1
        return total == num
