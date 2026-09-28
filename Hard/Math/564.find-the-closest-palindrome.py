"""
564. Find the Closest Palindrome
Difficulty: Hard
https://leetcode.com/problems/find-the-closest-palindrome/

──────────────────────────────────────────────────

Given a string n representing an integer, return the closest integer
(not including itself), which is a palindrome. If there is a tie,
return the smaller one.

The closest is defined as the absolute difference minimized between
two integers.

 

Example 1:

Input: n = "123"
Output: "121"

Example 2:

Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the
smallest which is 0.

 

Constraints:

	• 1 <= n.length <= 18

	• n consists of only digits.

	• n does not have leading zeros.

	• n is representing an integer in the range [1, 10^18 - 1].
"""

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        candidates = set()
        candidates.add(10 ** length + 1)
        candidates.add(10 ** (length - 1) - 1)
        prefix = int(n[:(length + 1) // 2])
        for delta in (-1, 0, 1):
            half = str(prefix + delta)
            if length % 2:
                candidate = half + half[-2::-1]
            else:
                candidate = half + half[::-1]
            candidates.add(int(candidate))
        number = int(n)
        best = None
        for candidate in candidates:
            if candidate == number:
                continue
            if best is None or (abs(candidate - number), candidate) < (abs(best - number), best):
                best = candidate
        return str(best)
