"""
2025. Maximum Number of Ways to Partition an Array
Difficulty: Hard
https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/

──────────────────────────────────────────────────

You are given a 0-indexed integer array nums of length n. The number
of ways to partition nums is the number of pivot indices that satisfy
both conditions:

	• 1 <= pivot < n

• nums[0] + nums[1] + ... + nums[pivot - 1] == nums[pivot] +
nums[pivot + 1] + ... + nums[n - 1]

You are also given an integer k. You can choose to change the value
of one element of nums to k, or to leave the array unchanged.

Return the maximum possible number of ways to partition nums to
satisfy both conditions after changing at most one element.

 

Example 1:

Input: nums = [2,-1,2], k = 3
Output: 1
Explanation: One optimal approach is to change nums[0] to k. The
array becomes [3,-1,2].
There is one way to partition the array:
- For pivot = 2, we have the partition [3,-1 | 2]: 3 + -1 == 2.

Example 2:

Input: nums = [0,0,0], k = 1
Output: 2
Explanation: The optimal approach is to leave the array unchanged.
There are two ways to partition the array:
- For pivot = 1, we have the partition [0 | 0,0]: 0 == 0 + 0.
- For pivot = 2, we have the partition [0,0 | 0]: 0 + 0 == 0.

Example 3:

Input: nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14], k = -33
Output: 4
Explanation: One optimal approach is to change nums[2] to k. The
array becomes [22,4,-33,-20,-15,15,-16,7,19,-10,0,-13,-14].
There are four ways to partition the array.

 

Constraints:

	• n == nums.length

	• 2 <= n <= 10^5

	• -10^5 <= k, nums[i] <= 10^5
"""

from collections import Counter


class Solution:
    def waysToPartition(self, nums: list[int], k: int) -> int:
        n = len(nums)
        total = sum(nums)
        prefix = [0] * (n + 1)
        for i, v in enumerate(nums):
            prefix[i + 1] = prefix[i] + v

        base = 0
        for j in range(1, n):
            if 2 * prefix[j] == total:
                base += 1

        left = Counter()
        right = Counter(prefix[1:n])
        best = base
        for i in range(n):
            delta = k - nums[i]
            cur = 0
            if (total - delta) % 2 == 0:
                cur += right[(total - delta) // 2]
            if (total + delta) % 2 == 0:
                cur += left[(total + delta) // 2]
            if cur > best:
                best = cur
            if i + 1 < n:
                p = prefix[i + 1]
                right[p] -= 1
                left[p] += 1
        return best
