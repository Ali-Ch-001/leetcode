"""
343. Integer Break
Difficulty: Medium
https://leetcode.com/problems/integer-break/

──────────────────────────────────────────────────

Given an integer n, break it into the sum of k positive integers,
where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

 

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 &times; 1 = 1.

Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 &times; 3 &times; 4 = 36.

 

Constraints:

	• 2 <= n <= 58
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        product = 1
        while n > 4:
            product *= 3
            n -= 3
        return product * n
