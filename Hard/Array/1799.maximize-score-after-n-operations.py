"""
1799. Maximize Score After N Operations
Difficulty: Hard
https://leetcode.com/problems/maximize-score-after-n-operations/

──────────────────────────────────────────────────

You are given nums, an array of positive integers of size 2 * n. You
must perform n operations on this array.

In the i^th operation (1-indexed), you will:

	• Choose two elements, x and y.

	• Receive a score of i * gcd(x, y).

	• Remove x and y from nums.

Return the maximum score you can receive after performing n
operations.

The function gcd(x, y) is the greatest common divisor of x and y.

 

Example 1:

Input: nums = [1,2]
Output: 1
Explanation: The optimal choice of operations is:
(1 * gcd(1, 2)) = 1

Example 2:

Input: nums = [3,4,6,8]
Output: 11
Explanation: The optimal choice of operations is:
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11

Example 3:

Input: nums = [1,2,3,4,5,6]
Output: 14
Explanation: The optimal choice of operations is:
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14

 

Constraints:

	• 1 <= n <= 7

	• nums.length == 2 * n

	• 1 <= nums[i] <= 10^6
"""

from math import gcd

class Solution:
    def maxScore(self, nums: list[int]) -> int:
        m = len(nums)
        dp = [0] * (1 << m)
        for mask in range(1 << m):
            used = bin(mask).count("1")
            if used % 2:
                continue
            step = used // 2 + 1
            rest = [i for i in range(m) if not (mask >> i) & 1]
            for a in range(len(rest)):
                for b in range(a + 1, len(rest)):
                    i, j = rest[a], rest[b]
                    nm = mask | (1 << i) | (1 << j)
                    val = dp[mask] + step * gcd(nums[i], nums[j])
                    if val > dp[nm]:
                        dp[nm] = val
        return dp[(1 << m) - 1]

