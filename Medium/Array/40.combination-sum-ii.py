"""
40. Combination Sum II
Difficulty: Medium
https://leetcode.com/problems/combination-sum-ii/

──────────────────────────────────────────────────

Given a collection of candidate numbers (candidates) and a target
number (target), find all unique combinations in candidates where the
candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

 

Constraints:

	• 1 <= candidates.length <= 100

	• 1 <= candidates[i] <= 50

	• 1 <= target <= 30
"""

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []
        candidates.sort()

        def backtrack(start: int, remaining: int, path: list[int]) -> None:
            if remaining == 0:
                results.append(path[:])
                return
            for i in range(start, len(candidates)):
                value = candidates[i]
                if value > remaining:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(value)
                backtrack(i + 1, remaining - value, path)
                path.pop()

        backtrack(0, target, [])
        return results
