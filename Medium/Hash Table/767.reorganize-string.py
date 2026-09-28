"""
767. Reorganize String
Difficulty: Medium
https://leetcode.com/problems/reorganize-string/

──────────────────────────────────────────────────

Given a string s, rearrange the characters of s so that any two
adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"

Example 2:

Input: s = "aaab"
Output: ""

 

Constraints:

	• 1 <= s.length <= 500

	• s consists of lowercase English letters.
"""

import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        if max(counts.values()) > (len(s) + 1) // 2:
            return ""
        heap = [(-count, ch) for ch, count in counts.items()]
        heapq.heapify(heap)
        result = []
        previous = None
        while heap:
            count, ch = heapq.heappop(heap)
            result.append(ch)
            count += 1
            if previous and previous[0] < 0:
                heapq.heappush(heap, previous)
            previous = (count, ch)
        return "".join(result)
