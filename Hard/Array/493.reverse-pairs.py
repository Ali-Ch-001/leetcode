"""
493. Reverse Pairs
Difficulty: Hard
https://leetcode.com/problems/reverse-pairs/

──────────────────────────────────────────────────

Given an integer array nums, return the number of reverse pairs in
the array.

A reverse pair is a pair (i, j) where:

	• 0 <= i < j < nums.length and

	• nums[i] > 2 * nums[j].

 

Example 1:

Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1

Example 2:

Input: nums = [2,4,3,5,1]
Output: 3
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1

 

Constraints:

	• 1 <= nums.length <= 5 * 10^4

	• -2^31 <= nums[i] <= 2^31 - 1
"""

class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        def merge_sort(values):
            if len(values) <= 1:
                return values, 0
            mid = len(values) // 2
            left, count_left = merge_sort(values[:mid])
            right, count_right = merge_sort(values[mid:])
            count = count_left + count_right
            j = 0
            for value in left:
                while j < len(right) and value > 2 * right[j]:
                    j += 1
                count += j
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

        _, result = merge_sort(nums)
        return result
