"""
164. Maximum Gap
Difficulty: Medium
https://leetcode.com/problems/maximum-gap/

──────────────────────────────────────────────────

Given an integer array nums, return the maximum difference between
two successive elements in its sorted form. If the array contains less
than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear
extra space.

 

Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6)
or (6,9) has the maximum difference 3.

Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore
return 0.

 

Constraints:

	• 1 <= nums.length <= 10^5

	• 0 <= nums[i] <= 10^9
"""

class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0
        low, high = min(nums), max(nums)
        if low == high:
            return 0
        n = len(nums)
        bucket_size = max(1, (high - low) // (n - 1))
        bucket_count = (high - low) // bucket_size + 1
        mins = [float("inf")] * bucket_count
        maxs = [float("-inf")] * bucket_count
        for value in nums:
            index = (value - low) // bucket_size
            mins[index] = min(mins[index], value)
            maxs[index] = max(maxs[index], value)
        best = 0
        previous = low
        for i in range(bucket_count):
            if mins[i] == float("inf"):
                continue
            best = max(best, mins[i] - previous)
            previous = maxs[i]
        return best
