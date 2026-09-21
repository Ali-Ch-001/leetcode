"""
179. Largest Number
Difficulty: Medium
https://leetcode.com/problems/largest-number/

──────────────────────────────────────────────────

Given a list of non-negative integers nums, arrange them such that
they form the largest number and return it.

Since the result may be very large, so you need to return a string
instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"

Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"

 

Constraints:

	• 1 <= nums.length <= 100

	• 0 <= nums[i] <= 10^9
"""

from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            return 1 if a + b < b + a else 0

        strings = [str(num) for num in nums]
        strings.sort(key=cmp_to_key(compare))
        result = "".join(strings)
        return "0" if result[0] == "0" else result
