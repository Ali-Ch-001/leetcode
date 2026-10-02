"""
1787. Make the XOR of All Segments Equal to Zero
Difficulty: Hard
https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/

──────────────────────────────────────────────────

You are given an array nums​​​ and an integer k​​​​​. The XOR of a
segment [left, right] where left <= right is the XOR of all the
elements with indices between left and right, inclusive: nums[left]
XOR nums[left+1] XOR ... XOR nums[right].

Return the minimum number of elements to change in the array such
that the XOR of all segments of size k​​​​​​ is equal to zero.

 

Example 1:

Input: nums = [1,2,0,3,0], k = 1
Output: 3
Explanation: Modify the array from [1,2,0,3,0] to from [0,0,0,0,0].

Example 2:

Input: nums = [3,4,5,2,1,7,3,4,7], k = 3
Output: 3
Explanation: Modify the array from [3,4,5,2,1,7,3,4,7] to
[3,4,7,3,4,7,3,4,7].

Example 3:

Input: nums = [1,2,4,1,2,5,1,2,6], k = 3
Output: 3
Explanation: Modify the array from [1,2,4,1,2,5,1,2,6] to
[1,2,3,1,2,3,1,2,3].

 

Constraints:

	• 1 <= k <= nums.length <= 2000

	• ​​​​​​0 <= nums[i] < 2^10
"""

class Solution:
    def minChanges(self, nums: list[int], k: int) -> int:
        from collections import Counter

        n = len(nums)
        groups = [Counter(nums[i::k]) for i in range(k)]
        NEG = -1
        dp = [NEG] * 1024
        dp[0] = 0
        for freq in groups:
            best = max(dp)
            ndp = [best] * 1024
            for j in range(1024):
                if dp[j] < 0:
                    continue
                base = dp[j]
                for v, c in freq.items():
                    t = j ^ v
                    if base + c > ndp[t]:
                        ndp[t] = base + c
            dp = ndp
        return n - dp[0]

