"""
152. Maximum Product Subarray
Difficulty: Medium
https://leetcode.com/problems/maximum-product-subarray/

──────────────────────────────────────────────────

Given an integer array nums, find a subarray that has the largest
product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit
integer.

Note that the product of an array with a single element is the value
of that element.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a
subarray.

 

Constraints:

	• 1 <= nums.length <= 2 * 10^4

	• -10 <= nums[i] <= 10

• The product of any subarray of nums is guaranteed to fit in a
32-bit integer.
"""

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        best = current_max = current_min = nums[0]
        for value in nums[1:]:
            candidates = (value, current_max * value, current_min * value)
            current_max = max(candidates)
            current_min = min(candidates)
            best = max(best, current_max)
        return best
