"""
327. Count of Range Sum
Difficulty: Hard
https://leetcode.com/problems/count-of-range-sum/

──────────────────────────────────────────────────

Given an integer array nums and two integers lower and upper, return
the number of range sums that lie in [lower, upper] inclusive.

Range sum S(i, j) is defined as the sum of the elements in nums
between indices i and j inclusive, where i <= j.

 

Example 1:

Input: nums = [-2,5,-1], lower = -2, upper = 2
Output: 3
Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their
respective sums are: -2, -1, 2.

Example 2:

Input: nums = [0], lower = 0, upper = 0
Output: 1

 

Constraints:

	• 1 <= nums.length <= 10^5

	• -2^31 <= nums[i] <= 2^31 - 1

	• -10^5 <= lower <= upper <= 10^5

	• The answer is guaranteed to fit in a 32-bit integer.
"""

class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)

        def merge_sort(values: list[int]) -> tuple[list[int], int]:
            if len(values) <= 1:
                return values, 0
            mid = len(values) // 2
            left, count_left = merge_sort(values[:mid])
            right, count_right = merge_sort(values[mid:])
            count = count_left + count_right
            i = j = 0
            for value in left:
                while i < len(right) and right[i] - value < lower:
                    i += 1
                while j < len(right) and right[j] - value <= upper:
                    j += 1
                count += j - i
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged, count

        _, result = merge_sort(prefix)
        return result
