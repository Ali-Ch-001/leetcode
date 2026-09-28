"""
805. Split Array With Same Average
Difficulty: Hard
https://leetcode.com/problems/split-array-with-same-average/

──────────────────────────────────────────────────

You are given an integer array nums.

You should move each element of nums into one of the two arrays A and
B such that A and B are non-empty, and average(A) == average(B).

Return true if it is possible to achieve that and false otherwise.

Note that for an array arr, average(arr) is the sum of all the
elements of arr over the length of arr.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7,8]
Output: true
Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and
both of them have an average of 4.5.

Example 2:

Input: nums = [3,1]
Output: false

 

Constraints:

	• 1 <= nums.length <= 30

	• 0 <= nums[i] <= 10^4
"""

from functools import lru_cache


class Solution:
    def splitArraySameAverage(self, nums: list[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        nums.sort()

        @lru_cache(maxsize=None)
        def can_pick(index, count, remaining):
            if count == 0:
                return remaining == 0
            if index == n or remaining < 0 or count > n - index:
                return False
            return can_pick(index + 1, count - 1, remaining - nums[index]) or can_pick(
                index + 1, count, remaining
            )

        for count in range(1, n):
            if total * count % n == 0 and can_pick(0, count, total * count // n):
                return True
        return False
