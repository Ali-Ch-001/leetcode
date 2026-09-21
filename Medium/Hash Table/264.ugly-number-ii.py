"""
264. Ugly Number II
Difficulty: Medium
https://leetcode.com/problems/ugly-number-ii/

──────────────────────────────────────────────────

An ugly number is a positive integer whose prime factors are limited
to 2, 3, and 5.

Given an integer n, return the n^th ugly number.

 

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the
first 10 ugly numbers.

Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime
factors are limited to 2, 3, and 5.

 

Constraints:

	• 1 <= n <= 1690
"""

import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = {1}
        current = 1
        for _ in range(n):
            current = heapq.heappop(heap)
            for factor in (2, 3, 5):
                nxt = current * factor
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)
        return current
