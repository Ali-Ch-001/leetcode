"""
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Difficulty: Medium
https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

──────────────────────────────────────────────────

Given an array of integers nums and an integer limit, return the size
of the longest non-empty subarray such that the absolute difference
between any two elements of this subarray is less than or equal to
limit.

 

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.

Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum
absolute diff is |2-7| = 5 <= 5.

Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3

 

Constraints:

	• 1 <= nums.length <= 10^5

	• 1 <= nums[i] <= 10^9

	• 0 <= limit <= 10^9
"""

class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        from collections import deque
        maxq = deque()
        minq = deque()
        left = 0
        best = 0
        for right, v in enumerate(nums):
            while maxq and nums[maxq[-1]] <= v:
                maxq.pop()
            maxq.append(right)
            while minq and nums[minq[-1]] >= v:
                minq.pop()
            minq.append(right)
            while nums[maxq[0]] - nums[minq[0]] > limit:
                left += 1
                if maxq[0] < left:
                    maxq.popleft()
                if minq[0] < left:
                    minq.popleft()
            best = max(best, right - left + 1)
        return best
