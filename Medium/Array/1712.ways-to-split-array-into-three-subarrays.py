"""
1712. Ways to Split Array Into Three Subarrays
Difficulty: Medium
https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

──────────────────────────────────────────────────

A split of an integer array is good if:

• The array is split into three non-empty contiguous subarrays -
named left, mid, right respectively from left to right.

• The sum of the elements in left is less than or equal to the sum
of the elements in mid, and the sum of the elements in mid is less
than or equal to the sum of the elements in right.

Given nums, an array of non-negative integers, return the number of
good ways to split nums. As the number may be too large, return it
modulo 10^9 + 7.

 

Example 1:

Input: nums = [1,1,1]
Output: 1
Explanation: The only good way to split nums is [1] [1] [1].

Example 2:

Input: nums = [1,2,2,2,5,0]
Output: 3
Explanation: There are three good ways of splitting nums:
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]

Example 3:

Input: nums = [3,2,1]
Output: 0
Explanation: There is no good way to split nums.

 

Constraints:

	• 3 <= nums.length <= 10^5

	• 0 <= nums[i] <= 10^4
"""

from bisect import bisect_left, bisect_right


class Solution:
    def waysToSplit(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        pre = [0] * (n + 1)
        for i, v in enumerate(nums):
            pre[i + 1] = pre[i] + v
        total = pre[n]
        ans = 0
        for i in range(1, n - 1):
            left = pre[i]
            lo = bisect_left(pre, 2 * left, i + 1, n)
            hi = bisect_right(pre, (total + left) // 2, i + 1, n) - 1
            if hi >= lo:
                ans = (ans + hi - lo + 1) % MOD
        return ans
