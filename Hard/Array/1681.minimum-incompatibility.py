"""
1681. Minimum Incompatibility
Difficulty: Hard
https://leetcode.com/problems/minimum-incompatibility/

──────────────────────────────────────────────────

You are given an integer array nums​​​ and an integer k. You are
asked to distribute this array into k subsets of equal size such that
there are no two equal elements in the same subset.

A subset's incompatibility is the difference between the maximum and
minimum elements in that array.

Return the minimum possible sum of incompatibilities of the k subsets
after distributing the array optimally, or return -1 if it is not
possible.

A subset is a group integers that appear in the array with no
particular order.

 

Example 1:

Input: nums = [1,2,1,4], k = 2
Output: 4
Explanation: The optimal distribution of subsets is [1,2] and [1,4].
The incompatibility is (2-1) + (4-1) = 4.
Note that [1,1] and [2,4] would result in a smaller sum, but the
first subset contains 2 equal elements.

Example 2:

Input: nums = [6,3,8,1,3,1,2,2], k = 4
Output: 6
Explanation: The optimal distribution of subsets is [1,2], [2,3],
[6,8], and [1,3].
The incompatibility is (2-1) + (3-2) + (8-6) + (3-1) = 6.

Example 3:

Input: nums = [5,3,3,6,3,3], k = 3
Output: -1
Explanation: It is impossible to distribute nums into 3 subsets where
no two elements are equal in the same subset.

 

Constraints:

	• 1 <= k <= nums.length <= 16

	• nums.length is divisible by k

	• 1 <= nums[i] <= nums.length
"""

from collections import Counter

class Solution:
    def minimumIncompatibility(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return 0
        sz = n // k
        if max(Counter(nums).values()) > k:
            return -1
        size = 1 << n
        by_low = [[] for _ in range(n)]
        for mask in range(1, size):
            if bin(mask).count("1") != sz:
                continue
            vals = [nums[i] for i in range(n) if (mask >> i) & 1]
            if len(set(vals)) == sz:
                low = (mask & -mask).bit_length() - 1
                by_low[low].append((mask, max(vals) - min(vals)))
        INF = float("inf")
        dp = [INF] * size
        dp[0] = 0
        full = size - 1
        for mask in range(size):
            cur = dp[mask]
            if cur == INF:
                continue
            rest = full ^ mask
            if not rest:
                continue
            low = (rest & -rest).bit_length() - 1
            for sub, c in by_low[low]:
                if sub & mask == 0:
                    nm = mask | sub
                    v = cur + c
                    if v < dp[nm]:
                        dp[nm] = v
        ans = dp[full]
        return ans if ans != INF else -1
