"""
1802. Maximum Value at a Given Index in a Bounded Array
Difficulty: Medium
https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

──────────────────────────────────────────────────

You are given three positive integers: n, index, and maxSum. You want
to construct an array nums (0-indexed) that satisfies the following
conditions:

	• nums.length == n

	• nums[i] is a positive integer where 0 <= i < n.

	• abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.

	• The sum of all the elements of nums does not exceed maxSum.

	• nums[index] is maximized.

Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.

 

Example 1:

Input: n = 4, index = 2,  maxSum = 6
Output: 2
Explanation: nums = [1,2,2,1] is one array that satisfies all the
conditions.
There are no arrays that satisfy all the conditions and have nums[2]
== 3, so 2 is the maximum nums[2].

Example 2:

Input: n = 6, index = 1,  maxSum = 10
Output: 3

 

Constraints:

	• 1 <= n <= maxSum <= 10^9

	• 0 <= index < n
"""

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def side_sum(length: int, peak: int) -> int:
            d = min(length, peak - 1)
            s = d * (2 * peak - d - 1) // 2
            if length > d:
                s += length - d
            return s

        def feasible(v: int) -> bool:
            total = v + side_sum(index, v) + side_sum(n - 1 - index, v)
            return total <= maxSum

        lo, hi = 1, maxSum
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo

