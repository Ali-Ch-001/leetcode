"""
718. Maximum Length of Repeated Subarray
Difficulty: Medium
https://leetcode.com/problems/maximum-length-of-repeated-subarray/

──────────────────────────────────────────────────

Given two integer arrays nums1 and nums2, return the maximum length
of a subarray that appears in both arrays.

 

Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
Explanation: The repeated subarray with maximum length is [0,0,0,0,0].

 

Constraints:

	• 1 <= nums1.length, nums2.length <= 1000

	• 0 <= nums1[i], nums2[i] <= 100
"""

class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [0] * (n + 1)
        best = 0
        for i in range(1, m + 1):
            current = [0] * (n + 1)
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    current[j] = dp[j - 1] + 1
                    best = max(best, current[j])
            dp = current
        return best
