"""
866. Prime Palindrome
Difficulty: Medium
https://leetcode.com/problems/prime-palindrome/

──────────────────────────────────────────────────

Given an integer n, return the smallest prime palindrome greater than
or equal to n.

An integer is prime if it has exactly two divisors: 1 and itself.
Note that 1 is not a prime number.

	• For example, 2, 3, 5, 7, 11, and 13 are all primes.

An integer is a palindrome if it reads the same from left to right as
it does from right to left.

	• For example, 101 and 12321 are palindromes.

The test cases are generated so that the answer always exists and is
in the range [2, 2 * 10^8].

 

Example 1:

Input: n = 6
Output: 7

Example 2:

Input: n = 8
Output: 11

Example 3:

Input: n = 13
Output: 101

 

Constraints:

	• 1 <= n <= 10^8
"""

class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(value):
            if value < 2:
                return False
            if value % 2 == 0:
                return value == 2
            divisor = 3
            while divisor * divisor <= value:
                if value % divisor == 0:
                    return False
                divisor += 2
            return True

        if n <= 2:
            return 2
        if n % 2 == 0:
            n += 1
        while True:
            if n > 11 and len(str(n)) % 2 == 0:
                n = 10 ** len(str(n)) + 1
            text = str(n)
            if text == text[::-1] and is_prime(n):
                return n
            n += 2
