"""
1862. Sum of Floored Pairs
Difficulty: Hard
https://leetcode.com/problems/sum-of-floored-pairs/

──────────────────────────────────────────────────

Given an integer array nums, return the sum of floor(nums[i] /
nums[j]) for all pairs of indices 0 <= i, j < nums.length in the
array. Since the answer may be too large, return it modulo 10^9 + 7.

The floor() function returns the integer part of the division.

 

Example 1:

Input: nums = [2,5,9]
Output: 10
Explanation:
floor(2 / 5) = floor(2 / 9) = floor(5 / 9) = 0
floor(2 / 2) = floor(5 / 5) = floor(9 / 9) = 1
floor(5 / 2) = 2
floor(9 / 2) = 4
floor(9 / 5) = 1
We calculate the floor of the division for every pair of indices in
the array then sum them up.

Example 2:

Input: nums = [7,7,7,7,7,7,7]
Output: 49

 

Constraints:

	• 1 <= nums.length <= 10^5

	• 1 <= nums[i] <= 10^5
"""

class Solution:
    def sumOfFlooredPairs(self, nums: list[int]) -> int:
        MOD = 10 ** 9 + 7
        M = max(nums)
        freq = [0] * (M + 1)
        for x in nums:
            freq[x] += 1
        prefix = [0] * (M + 1)
        for i in range(1, M + 1):
            prefix[i] = prefix[i - 1] + freq[i]
        ans = 0
        for d in range(1, M + 1):
            c = freq[d]
            if c == 0:
                continue
            m = 1
            while m * d <= M:
                hi = min((m + 1) * d - 1, M)
                count = prefix[hi] - prefix[m * d - 1]
                ans = (ans + c * count * m) % MOD
                m += 1
        return ans
