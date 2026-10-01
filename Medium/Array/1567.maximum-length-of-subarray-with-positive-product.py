"""
1567. Maximum Length of Subarray With Positive Product
Difficulty: Medium
https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

──────────────────────────────────────────────────

Given an array of integers nums, find the maximum length of a
subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more
values taken out of that array.

Return the maximum length of a subarray with positive product.

 

Example 1:

Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.

Example 2:

Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3]
which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make
the product 0 which is not positive.

Example 3:

Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or
[-2,-3].

 

Constraints:

	• 1 <= nums.length <= 10^5

	• -10^9 <= nums[i] <= 10^9
"""

class Solution:
    def getMaxLen(self, nums: list[int]) -> int:
        pos = neg = 0
        ans = 0
        for x in nums:
            if x == 0:
                pos = neg = 0
            elif x > 0:
                pos += 1
                neg = neg + 1 if neg else 0
            else:
                new_pos = neg + 1 if neg else 0
                new_neg = pos + 1
                pos, neg = new_pos, new_neg
            if pos > ans:
                ans = pos
        return ans
