"""
76. Minimum Window Substring
Difficulty: Hard
https://leetcode.com/problems/minimum-window-substring/

──────────────────────────────────────────────────

Given two strings s and t of lengths m and n respectively, return the
minimum window substring of s such that every character in t
(including duplicates) is included in the window. If there is no such
substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B',
and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

 

Constraints:

	• m == s.length

	• n == t.length

	• 1 <= m, n <= 10^5

	• s and t consist of uppercase and lowercase English letters.

 

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        missing = len(t)
        best_left = best_right = 0
        best_len = float("inf")
        left = 0
        for right, ch in enumerate(s):
            if ch in need:
                if need[ch] > 0:
                    missing -= 1
                need[ch] -= 1
            while missing == 0:
                if right - left + 1 < best_len:
                    best_left, best_right = left, right
                    best_len = right - left + 1
                left_ch = s[left]
                if left_ch in need:
                    need[left_ch] += 1
                    if need[left_ch] > 0:
                        missing += 1
                left += 1
        return s[best_left:best_right + 1] if best_len != float("inf") else ""
