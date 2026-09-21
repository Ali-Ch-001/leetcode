"""
220. Contains Duplicate III
Difficulty: Hard
https://leetcode.com/problems/contains-duplicate-iii/

──────────────────────────────────────────────────

You are given an integer array nums and two integers indexDiff and
valueDiff.

Find a pair of indices (i, j) such that:

	• i != j,

	• abs(i - j) <= indexDiff.

	• abs(nums[i] - nums[j]) <= valueDiff, and

Return true if such pair exists or false otherwise.

 

Example 1:

Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: We can choose (i, j) = (0, 3).
We satisfy the three conditions:
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0

Example 2:

Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output: false
Explanation: After trying all the possible pairs (i, j), we cannot
satisfy the three conditions, so we return false.

 

Constraints:

	• 2 <= nums.length <= 10^5

	• -10^9 <= nums[i] <= 10^9

	• 1 <= indexDiff <= nums.length

	• 0 <= valueDiff <= 10^9
"""

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0 or indexDiff <= 0:
            return False
        buckets = {}
        size = valueDiff + 1
        for i, value in enumerate(nums):
            bucket = value // size
            if bucket in buckets:
                return True
            if bucket - 1 in buckets and value - buckets[bucket - 1] <= valueDiff:
                return True
            if bucket + 1 in buckets and buckets[bucket + 1] - value <= valueDiff:
                return True
            buckets[bucket] = value
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // size]
        return False
