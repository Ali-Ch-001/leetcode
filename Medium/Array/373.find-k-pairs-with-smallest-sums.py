"""
373. Find K Pairs with Smallest Sums
Difficulty: Medium
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

──────────────────────────────────────────────────

You are given two integer arrays nums1 and nums2 sorted in
non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first
array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the
smallest sums.

 

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

 

Constraints:

	• 1 <= nums1.length, nums2.length <= 10^5

	• -10^9 <= nums1[i], nums2[i] <= 10^9

	• nums1 and nums2 both are sorted in non-decreasing order.

	• 1 <= k <= 10^4

	• k <= nums1.length * nums2.length
"""

import heapq


class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        if not nums1 or not nums2:
            return []
        heap = [(nums1[0] + nums2[0], 0, 0)]
        seen = {(0, 0)}
        result = []
        while heap and len(result) < k:
            _, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1) and (i + 1, j) not in seen:
                seen.add((i + 1, j))
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            if j + 1 < len(nums2) and (i, j + 1) not in seen:
                seen.add((i, j + 1))
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return result
