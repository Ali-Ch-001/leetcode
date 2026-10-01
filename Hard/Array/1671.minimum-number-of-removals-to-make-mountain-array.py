"""
1671. Minimum Number of Removals to Make Mountain Array
Difficulty: Hard
https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

──────────────────────────────────────────────────

You may recall that an array arr is a mountain array if and only if:

	• arr.length >= 3

• There exists some index i (0-indexed) with 0 < i < arr.length - 1
such that:
	
		• arr[0] < arr[1] < ... < arr[i - 1] < arr[i]

		• arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

	
	

Given an integer array nums​​​, return the minimum number of elements
to remove to make nums​​​ a mountain array.

 

Example 1:

Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need
to remove any elements.

Example 2:

Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1,
and 5, making the array nums = [1,5,6,3,1].

 

Constraints:

	• 3 <= nums.length <= 1000

	• 1 <= nums[i] <= 10^9

	• It is guaranteed that you can make a mountain array out of nums.
"""

class Solution:
    def minimumMountainRemovals(self, nums: list[int]) -> int:
        n = len(nums)
        inc = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and inc[j] + 1 > inc[i]:
                    inc[i] = inc[j] + 1
        dec = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] < nums[i] and dec[j] + 1 > dec[i]:
                    dec[i] = dec[j] + 1
        best = 0
        for i in range(n):
            if inc[i] > 1 and dec[i] > 1:
                length = inc[i] + dec[i] - 1
                if length > best:
                    best = length
        return n - best
