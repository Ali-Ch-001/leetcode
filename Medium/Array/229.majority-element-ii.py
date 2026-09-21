"""
229. Majority Element II
Difficulty: Medium
https://leetcode.com/problems/majority-element-ii/

──────────────────────────────────────────────────

Given an integer array of size n, find all elements that appear more
than &lfloor;n / 3&rfloor; times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]

Example 2:

Input: nums = [1]
Output: [1]

Example 3:

Input: nums = [1,2]
Output: [1,2]

 

Constraints:

	• 1 <= nums.length <= 5 * 10^4

	• -10^9 <= nums[i] <= 10^9

 

Follow up: Could you solve the problem in linear time and in O(1)
space?
"""

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        first = second = None
        count1 = count2 = 0
        for value in nums:
            if value == first:
                count1 += 1
            elif value == second:
                count2 += 1
            elif count1 == 0:
                first = value
                count1 = 1
            elif count2 == 0:
                second = value
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        result = []
        for candidate in (first, second):
            if candidate is not None and nums.count(candidate) > len(nums) // 3:
                result.append(candidate)
        return result
