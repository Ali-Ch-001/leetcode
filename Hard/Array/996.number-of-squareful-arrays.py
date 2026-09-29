"""
996. Number of Squareful Arrays
Difficulty: Hard
https://leetcode.com/problems/number-of-squareful-arrays/

──────────────────────────────────────────────────

An array is squareful if the sum of every pair of adjacent elements
is a perfect square.

Given an integer array nums, return the number of permutations of
nums that are squareful.

Two permutations perm1 and perm2 are different if there is some index
i such that perm1[i] != perm2[i].

 

Example 1:

Input: nums = [1,17,8]
Output: 2
Explanation: [1,8,17] and [17,8,1] are the valid permutations.

Example 2:

Input: nums = [2,2,2]
Output: 1

 

Constraints:

	• 1 <= nums.length <= 12

	• 0 <= nums[i] <= 10^9
"""

import math


class Solution:
    def numSquarefulPerms(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        used = [False] * n
        count = 0

        def is_square(value):
            root = math.isqrt(value)
            return root * root == value

        def backtrack(previous):
            nonlocal count
            if all(used):
                count += 1
                return
            seen = set()
            for i in range(n):
                if used[i] or nums[i] in seen:
                    continue
                if previous is not None and not is_square(previous + nums[i]):
                    continue
                seen.add(nums[i])
                used[i] = True
                backtrack(nums[i])
                used[i] = False

        backtrack(None)
        return count
