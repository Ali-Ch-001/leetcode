"""
1224. Maximum Equal Frequency
Difficulty: Hard
https://leetcode.com/problems/maximum-equal-frequency/

──────────────────────────────────────────────────

Given an array nums of positive integers, return the longest possible
length of an array prefix of nums, such that it is possible to remove
exactly one element from this prefix so that every number that has
appeared in it will have the same number of occurrences.

If after removing one element there are no remaining elements, it's
still considered that every appeared number has the same number of
ocurrences (0).

 

Example 1:

Input: nums = [2,2,1,1,5,3,3,5]
Output: 7
Explanation: For the subarray [2,2,1,1,5,3,3] of length 7, if we
remove nums[4] = 5, we will get [2,2,1,1,3,3], so that each number
will appear exactly twice.

Example 2:

Input: nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
Output: 13

 

Constraints:

	• 2 <= nums.length <= 10^5

	• 1 <= nums[i] <= 10^5
"""

class Solution:
    def maxEqualFreq(self, nums: list[int]) -> int:
        cnt: dict[int, int] = {}
        freq: dict[int, int] = {}
        best = 0
        maxf = 0
        for i, x in enumerate(nums, 1):
            c = cnt.get(x, 0)
            if c > 0:
                freq[c] -= 1
                if freq[c] == 0:
                    del freq[c]
            cnt[x] = c + 1
            freq[c + 1] = freq.get(c + 1, 0) + 1
            if c + 1 > maxf:
                maxf = c + 1
            d = len(cnt)
            if maxf == 1:
                best = i
            elif freq.get(maxf, 0) == 1 and freq.get(maxf - 1, 0) == d - 1:
                best = i
            elif freq.get(1, 0) == 1 and freq.get(maxf, 0) == d - 1:
                best = i
        return best
        
