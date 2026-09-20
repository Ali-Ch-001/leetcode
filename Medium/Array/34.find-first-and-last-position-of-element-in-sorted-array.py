"""
34. Find First and Last Position of Element in Sorted Array
Difficulty: Medium
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

──────────────────────────────────────────────────

Given an array of integers nums sorted in non-decreasing order, find
the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

 

Constraints:

	• 0 <= nums.length <= 10^5

	• -10^9 <= nums[i] <= 10^9

	• nums is a non-decreasing array.

	• -10^9 <= target <= 10^9
"""

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def bound(find_first: bool) -> int:
            lo, hi = 0, len(nums) - 1
            result = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    result = mid
                    if find_first:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return result

        return [bound(True), bound(False)]
