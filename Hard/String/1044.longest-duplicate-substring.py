"""
1044. Longest Duplicate Substring
Difficulty: Hard
https://leetcode.com/problems/longest-duplicate-substring/

──────────────────────────────────────────────────

Given a string s, consider all duplicated substrings: (contiguous)
substrings of s that occur 2 or more times. The occurrences may
overlap.

Return any duplicated substring that has the longest possible length.
If s does not have a duplicated substring, the answer is "".

 

Example 1:

Input: s = "banana"
Output: "ana"

Example 2:

Input: s = "abcd"
Output: ""

 

Constraints:

	• 2 <= s.length <= 3 * 10^4

	• s consists of lowercase English letters.
"""

import random

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        m1 = (1 << 61) - 1
        m2 = (1 << 31) - 1
        b1 = random.randrange(256, 1 << 20)
        b2 = random.randrange(256, 1 << 20)

        def check(length: int) -> int:
            h1 = h2 = 0
            for i in range(length):
                h1 = (h1 * b1 + ord(s[i])) % m1
                h2 = (h2 * b2 + ord(s[i])) % m2
            p1 = pow(b1, length, m1)
            p2 = pow(b2, length, m2)
            seen = {(h1, h2)}
            for i in range(1, n - length + 1):
                h1 = (h1 * b1 - ord(s[i - 1]) * p1 + ord(s[i + length - 1])) % m1
                h2 = (h2 * b2 - ord(s[i - 1]) * p2 + ord(s[i + length - 1])) % m2
                key = (h1, h2)
                if key in seen:
                    return i
                seen.add(key)
            return -1

        lo, hi = 1, n - 1
        best_start, best_len = 0, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            pos = check(mid)
            if pos != -1:
                best_start, best_len = pos, mid
                lo = mid + 1
            else:
                hi = mid - 1
        return s[best_start:best_start + best_len]
