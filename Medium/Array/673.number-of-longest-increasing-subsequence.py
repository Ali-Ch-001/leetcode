"""
673. Number of Longest Increasing Subsequence
Difficulty: Medium
https://leetcode.com/problems/number-of-longest-increasing-subsequence/

──────────────────────────────────────────────────

Given an integer array nums, return the number of longest increasing
subsequences.

Notice that the sequence has to be strictly increasing.

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7]
and [1, 3, 5, 7].

Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1,
and there are 5 increasing subsequences of length 1, so output 5.

 

Constraints:

	• 1 <= nums.length <= 2000

	• -10^6 <= nums[i] <= 10^6

	• The answer is guaranteed to fit inside a 32-bit integer.
"""

class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        lengths = [1] * n
        counts = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]
        best = max(lengths)
        return sum(counts[i] for i in range(n) if lengths[i] == best)
