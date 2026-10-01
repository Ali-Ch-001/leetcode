"""
1424. Diagonal Traverse II
Difficulty: Medium
https://leetcode.com/problems/diagonal-traverse-ii/

──────────────────────────────────────────────────

Given a 2D integer array nums, return all elements of nums in
diagonal order as shown in the below images.

 

Example 1:

Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]

Example 2:

Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

 

Constraints:

	• 1 <= nums.length <= 10^5

	• 1 <= nums[i].length <= 10^5

	• 1 <= sum(nums[i].length) <= 10^5

	• 1 <= nums[i][j] <= 10^5
"""

class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        diagonals = {}
        max_d = 0
        for i, row in enumerate(nums):
            for j, v in enumerate(row):
                d = i + j
                if d not in diagonals:
                    diagonals[d] = []
                diagonals[d].append(v)
                if d > max_d:
                    max_d = d
        res = []
        for d in range(max_d + 1):
            if d in diagonals:
                res.extend(reversed(diagonals[d]))
        return res
