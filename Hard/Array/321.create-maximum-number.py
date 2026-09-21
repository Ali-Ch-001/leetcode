"""
321. Create Maximum Number
Difficulty: Hard
https://leetcode.com/problems/create-maximum-number/

──────────────────────────────────────────────────

You are given two integer arrays nums1 and nums2 of lengths m and n
respectively. nums1 and nums2 represent the digits of two numbers. You
are also given an integer k.

Create the maximum number of length k <= m + n from digits of the two
numbers. The relative order of the digits from the same array must be
preserved.

Return an array of the k digits representing the answer.

 

Example 1:

Input: nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
Output: [9,8,6,5,3]

Example 2:

Input: nums1 = [6,7], nums2 = [6,0,4], k = 5
Output: [6,7,6,0,4]

Example 3:

Input: nums1 = [3,9], nums2 = [8,9], k = 3
Output: [9,8,9]

 

Constraints:

	• m == nums1.length

	• n == nums2.length

	• 1 <= m, n <= 500

	• 0 <= nums1[i], nums2[i] <= 9

	• 1 <= k <= m + n

	• nums1 and nums2 do not have leading zeros.
"""

class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        def best_single(nums: list[int], count: int) -> list[int]:
            drop = len(nums) - count
            stack = []
            for value in nums:
                while drop > 0 and stack and stack[-1] < value:
                    stack.pop()
                    drop -= 1
                stack.append(value)
            return stack[:count]

        def merge(a: list[int], b: list[int]) -> list[int]:
            result = []
            i = j = 0
            while i < len(a) or j < len(b):
                if j == len(b) or (i < len(a) and a[i:] > b[j:]):
                    result.append(a[i])
                    i += 1
                else:
                    result.append(b[j])
                    j += 1
            return result

        best = []
        for take1 in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            candidate = merge(best_single(nums1, take1), best_single(nums2, k - take1))
            if candidate > best:
                best = candidate
        return best
