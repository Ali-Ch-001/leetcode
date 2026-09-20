"""
47. Permutations II
Difficulty: Medium
https://leetcode.com/problems/permutations-ii/

──────────────────────────────────────────────────

Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

 

Constraints:

	• 1 <= nums.length <= 8

	• -10 <= nums[i] <= 10
"""

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        results = []
        nums.sort()
        used = [False] * len(nums)

        def backtrack(path: list[int]) -> None:
            if len(path) == len(nums):
                results.append(path[:])
                return
            for i, value in enumerate(nums):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(value)
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return results
