"""
906. Super Palindromes
Difficulty: Hard
https://leetcode.com/problems/super-palindromes/

──────────────────────────────────────────────────

Let's say a positive integer is a super-palindrome if it is a
palindrome, and it is also the square of a palindrome.

Given two positive integers left and right represented as strings,
return the number of super-palindromes integers in the inclusive range
[left, right].

 

Example 1:

Input: left = "4", right = "1000"
Output: 4
Explanation: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not
a palindrome.

Example 2:

Input: left = "1", right = "2"
Output: 1

 

Constraints:

	• 1 <= left.length, right.length <= 18

	• left and right consist of only digits.

	• left and right cannot have leading zeros.

	• left and right represent integers in the range [1, 10^18 - 1].

	• left is less than or equal to right.
"""

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        low, high = int(left), int(right)
        count = 0
        limit = int(high ** 0.5) + 1

        def is_palindrome(value):
            text = str(value)
            return text == text[::-1]

        for root in range(1, min(limit, 100000) + 1):
            text = str(root)
            for candidate in (int(text + text[-2::-1]), int(text + text[::-1])):
                square = candidate * candidate
                if low <= square <= high and is_palindrome(square):
                    count += 1
        return count
