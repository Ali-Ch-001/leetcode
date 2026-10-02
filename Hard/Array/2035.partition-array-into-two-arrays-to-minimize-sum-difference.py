"""
2035. Partition Array Into Two Arrays to Minimize Sum Difference
Difficulty: Hard
https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/

──────────────────────────────────────────────────

You are given an integer array nums of 2 * n integers. You need to
partition nums into two arrays of length n to minimize the absolute
difference of the sums of the arrays. To partition nums, put each
element of nums into one of the two arrays.

Return the minimum possible absolute difference.

 

Example 1:

Input: nums = [3,9,7,3]
Output: 2
Explanation: One optimal partition is: [3,9] and [7,3].
The absolute difference between the sums of the arrays is abs((3 + 9)
- (7 + 3)) = 2.

Example 2:

Input: nums = [-36,36]
Output: 72
Explanation: One optimal partition is: [-36] and [36].
The absolute difference between the sums of the arrays is abs((-36) -
(36)) = 72.

Example 3:

Input: nums = [2,-1,0,4,-2,-9]
Output: 0
Explanation: One optimal partition is: [2,4,-9] and [-1,0,-2].
The absolute difference between the sums of the arrays is abs((2 + 4
+ -9) - (-1 + 0 + -2)) = 0.

 

Constraints:

	• 1 <= n <= 15

	• nums.length == 2 * n

	• -10^7 <= nums[i] <= 10^7
"""

from bisect import bisect_left


class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        n = len(nums) // 2
        total = sum(nums)

        def subset_sums(arr):
            size = len(arr)
            sums = [[] for _ in range(size + 1)]
            for mask in range(1 << size):
                s = 0
                cnt = 0
                for i in range(size):
                    if mask >> i & 1:
                        s += arr[i]
                        cnt += 1
                sums[cnt].append(s)
            return sums

        left_sums = subset_sums(nums[:n])
        right_sums = subset_sums(nums[n:])
        for lst in right_sums:
            lst.sort()

        best = float('inf')
        for i in range(n + 1):
            lst = right_sums[n - i]
            for s1 in left_sums[i]:
                target = (total - 2 * s1) / 2
                pos = bisect_left(lst, target)
                if pos < len(lst):
                    best = min(best, abs(total - 2 * (s1 + lst[pos])))
                if pos > 0:
                    best = min(best, abs(total - 2 * (s1 + lst[pos - 1])))
        return best
