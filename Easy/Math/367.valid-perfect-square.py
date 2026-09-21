"""
367. Valid Perfect Square
Difficulty: Easy
https://leetcode.com/problems/valid-perfect-square/

──────────────────────────────────────────────────

Given a positive integer num, return true if num is a perfect square
or false otherwise.

A perfect square is an integer that is the square of an integer. In
other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is
not an integer.

 

Constraints:

	• 1 <= num <= 2^31 - 1
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo, hi = 1, num
        while lo <= hi:
            mid = (lo + hi) // 2
            square = mid * mid
            if square == num:
                return True
            if square < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
