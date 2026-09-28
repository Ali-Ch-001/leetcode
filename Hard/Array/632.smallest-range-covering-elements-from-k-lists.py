"""
632. Smallest Range Covering Elements from K Lists
Difficulty: Hard
https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

──────────────────────────────────────────────────

You have k lists of sorted integers in non-decreasing order. Find the
smallest range that includes at least one number from each of the k
lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d
- c or a < c if b - a == d - c.

 

Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].

Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]

 

Constraints:

	• nums.length == k

	• 1 <= k <= 3500

	• 1 <= nums[i].length <= 50

	• -10^5 <= nums[i][j] <= 10^5

	• nums[i] is sorted in non-decreasing order.
"""

import heapq


class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        heap = []
        current_max = float("-inf")
        for i, row in enumerate(nums):
            heapq.heappush(heap, (row[0], i, 0))
            current_max = max(current_max, row[0])
        best_left, best_right = float("-inf"), float("inf")
        while True:
            current_min, row, index = heapq.heappop(heap)
            if current_max - current_min < best_right - best_left:
                best_left, best_right = current_min, current_max
            if index + 1 == len(nums[row]):
                return [best_left, best_right]
            nxt = nums[row][index + 1]
            heapq.heappush(heap, (nxt, row, index + 1))
            current_max = max(current_max, nxt)
