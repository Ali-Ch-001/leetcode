"""
1031. Maximum Sum of Two Non-Overlapping Subarrays
Difficulty: Medium
https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

──────────────────────────────────────────────────

Given an integer array nums and two integers firstLen and secondLen,
return the maximum sum of elements in two non-overlapping subarrays
with lengths firstLen and secondLen.

The array with length firstLen could occur before or after the array
with length secondLen, but they have to be non-overlapping.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5]
with length 2.

Example 2:

Input: nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and
[8,9] with length 2.

Example 3:

Input: nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and
[0,3,8] with length 3.

 

Constraints:

	• 1 <= firstLen, secondLen <= 1000

	• 2 <= firstLen + secondLen <= 1000

	• firstLen + secondLen <= nums.length <= 1000

	• 0 <= nums[i] <= 1000
"""

class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i, v in enumerate(nums):
            pre[i + 1] = pre[i] + v

        def best(a: int, b: int) -> int:
            res = 0
            best_a = 0
            for i in range(a, n + 1):
                best_a = max(best_a, pre[i] - pre[i - a])
                if i + b <= n:
                    res = max(res, best_a + pre[i + b] - pre[i])
            return res

        return max(best(firstLen, secondLen), best(secondLen, firstLen))
