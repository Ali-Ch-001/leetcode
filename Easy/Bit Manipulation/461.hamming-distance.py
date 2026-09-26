"""
461. Hamming Distance
Difficulty: Easy
https://leetcode.com/problems/hamming-distance/

──────────────────────────────────────────────────

The Hamming distance between two integers is the number of positions
at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

 

Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       &uarr;   &uarr;
The above arrows point to positions where the corresponding bits are
different.

Example 2:

Input: x = 3, y = 1
Output: 1

 

Constraints:

	• 0 <= x, y <= 2^31 - 1

 

Note: This question is the same as  2220: Minimum Bit Flips to
Convert Number.
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        value = x ^ y
        count = 0
        while value:
            value &= value - 1
            count += 1
        return count
