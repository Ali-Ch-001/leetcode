"""
1191. K-Concatenation Maximum Sum
Difficulty: Medium
https://leetcode.com/problems/k-concatenation-maximum-sum/

──────────────────────────────────────────────────

Given an integer array arr and an integer k, modify the array by
repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will
be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array. Note that the
length of the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: arr = [1,2], k = 3
Output: 9

Example 2:

Input: arr = [1,-2,1], k = 5
Output: 2

Example 3:

Input: arr = [-1,-2], k = 7
Output: 0

 

Constraints:

	• 1 <= arr.length <= 10^5

	• 1 <= k <= 10^5

	• -10^4 <= arr[i] <= 10^4
"""

class Solution:
    def kConcatenationMaxSum(self, arr: list[int], k: int) -> int:
        MOD = 10 ** 9 + 7

        def kadane(a):
            best = cur = 0
            for x in a:
                cur = max(0, cur + x)
                best = max(best, cur)
            return best

        if k == 1:
            return kadane(arr) % MOD
        best_mid = kadane(arr + arr)
        total = sum(arr)
        if total <= 0:
            return best_mid % MOD
        prefix = 0
        cur = 0
        for x in arr:
            cur += x
            prefix = max(prefix, cur)
        suffix = 0
        cur = 0
        for x in reversed(arr):
            cur += x
            suffix = max(suffix, cur)
        return max(best_mid, prefix + suffix + total * (k - 2)) % MOD
        
