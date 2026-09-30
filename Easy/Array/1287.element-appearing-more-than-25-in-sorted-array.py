"""
1287. Element Appearing More Than 25% In Sorted Array
Difficulty: Easy
https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

──────────────────────────────────────────────────

Given an integer array sorted in non-decreasing order, there is
exactly one integer in the array that occurs more than 25% of the
time, return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

Example 2:

Input: arr = [1,1]
Output: 1

 

Constraints:

	• 1 <= arr.length <= 10^4

	• 0 <= arr[i] <= 10^5
"""

class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        n = len(arr)
        count = 0
        prev = None
        for x in arr:
            if x == prev:
                count += 1
            else:
                prev = x
                count = 1
            if count > n / 4:
                return x
        return arr[-1]
