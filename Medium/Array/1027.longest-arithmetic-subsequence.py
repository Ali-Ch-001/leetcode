"""
1027. Longest Arithmetic Subsequence
Difficulty: Medium
https://leetcode.com/problems/longest-arithmetic-subsequence/

──────────────────────────────────────────────────

Given an array nums of integers, return the length of the longest
arithmetic subsequence in nums.

Note that:

• A subsequence is an array that can be derived from another array
by deleting some or no elements without changing the order of the
remaining elements.

• A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the
same value (for 0 <= i < seq.length - 1).

 

Example 1:

Input: nums = [3, 6, 9, 12]

Output: 4

Explanation: The whole array is already an arithmetic sequence with a
common difference of 3, so the longest arithmetic subsequence is [3,
6, 9, 12], of length 4.

Example 2:

Input: nums = [9, 4, 7, 2, 10]

Output: 3

Explanation: The longest arithmetic subsequence is [4, 7, 10]
(indices 1, 2, 4), with a common difference of 3. There is no
arithmetic subsequence of length 4.

Example 3:

Input: nums = [20, 1, 15, 3, 10, 5, 8]

Output: 4

Explanation: The longest arithmetic subsequence is [20, 15, 10, 5]
(indices 0, 2, 4, 5), with a common difference of -5.

 

Constraints:

	• 2 <= nums.length <= 1500

	• 0 <= nums[i] <= 500
"""

class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        dp = [{} for _ in nums]
        best = 2
        for i in range(len(nums)):
            for j in range(i):
                d = nums[i] - nums[j]
                cur = dp[j].get(d, 1) + 1
                dp[i][d] = cur
                if cur > best:
                    best = cur
        return best
