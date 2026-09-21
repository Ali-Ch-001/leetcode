"""
283. Move Zeroes
Difficulty: Easy
https://leetcode.com/problems/move-zeroes/

──────────────────────────────────────────────────

Given an integer array nums, move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the
array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

 

Constraints:

	• 1 <= nums.length <= 10^4

	• -2^31 <= nums[i] <= 2^31 - 1

 

Follow up: Could you minimize the total number of operations done?
"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insert = 0
        for value in nums:
            if value != 0:
                nums[insert] = value
                insert += 1
        for i in range(insert, len(nums)):
            nums[i] = 0
