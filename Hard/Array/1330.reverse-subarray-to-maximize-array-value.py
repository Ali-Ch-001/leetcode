"""
1330. Reverse Subarray To Maximize Array Value
Difficulty: Hard
https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/

──────────────────────────────────────────────────

You are given an integer array nums. The value of this array is
defined as the sum of |nums[i] - nums[i + 1]| for all 0 <= i <
nums.length - 1.

You are allowed to select any subarray of the given array and reverse
it. You can perform this operation only once.

Find maximum possible value of the final array.

 

Example 1:

Input: nums = [2,3,1,5,4]
Output: 10
Explanation: By reversing the subarray [3,1,5] the array becomes
[2,5,1,3,4] whose value is 10.

Example 2:

Input: nums = [2,4,9,24,2,1,10]
Output: 68

 

Constraints:

	• 2 <= nums.length <= 3 * 10^4

	• -10^5 <= nums[i] <= 10^5

	• The answer is guaranteed to fit in a 32-bit integer.
"""

class Solution:
    def maxValueAfterReverse(self, nums: list[int]) -> int:
        n = len(nums)
        base = sum(abs(nums[i + 1] - nums[i]) for i in range(n - 1))
        gain = 0
        for r in range(n - 1):
            gain = max(gain, abs(nums[0] - nums[r + 1]) - abs(nums[r] - nums[r + 1]))
        for l in range(1, n):
            gain = max(gain, abs(nums[l - 1] - nums[n - 1]) - abs(nums[l - 1] - nums[l]))
        NEG = float('-inf')
        best = [NEG] * 4
        for j in range(1, n - 1):
            i = j - 1
            ci = abs(nums[i] - nums[i + 1])
            p = (nums[i] + nums[i + 1] - ci,
                 nums[i] - nums[i + 1] - ci,
                 -nums[i] + nums[i + 1] - ci,
                 -nums[i] - nums[i + 1] - ci)
            for k in range(4):
                if p[k] > best[k]:
                    best[k] = p[k]
            cj = abs(nums[j] - nums[j + 1])
            q = (-(nums[j] + nums[j + 1]) - cj,
                 -nums[j] + nums[j + 1] - cj,
                 nums[j] - nums[j + 1] - cj,
                 nums[j] + nums[j + 1] - cj)
            for k in range(4):
                if best[k] + q[k] > gain:
                    gain = best[k] + q[k]
        return base + gain
        
