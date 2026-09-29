"""
896. Monotonic Array
Difficulty: Easy
https://leetcode.com/problems/monotonic-array/

──────────────────────────────────────────────────

An array is monotonic if it is either monotone increasing or monotone
decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <=
nums[j]. An array nums is monotone decreasing if for all i <= j,
nums[i] >= nums[j].

Given an integer array nums, return true if the given array is
monotonic, or false otherwise.

 

Example 1:

Input: nums = [1,2,2,3]
Output: true

Example 2:

Input: nums = [6,5,4,4]
Output: true

Example 3:

Input: nums = [1,3,2]
Output: false

 

Constraints:

	• 1 <= nums.length <= 10^5

	• -10^5 <= nums[i] <= 10^5
"""

class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        increasing = decreasing = True
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing = False
            elif nums[i] < nums[i - 1]:
                increasing = False
        return increasing or decreasing
