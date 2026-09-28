"""
567. Permutation in String
Difficulty: Medium
https://leetcode.com/problems/permutation-in-string/

──────────────────────────────────────────────────

Given two strings s1 and s2, return true if s2 contains a permutation
of s1, or false otherwise.

In other words, return true if one of s1's permutations is the
substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

 

Constraints:

	• 1 <= s1.length, s2.length <= 10^4

	• s1 and s2 consist of lowercase English letters.
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = [0] * 26
        window = [0] * 26
        for ch in s1:
            need[ord(ch) - 97] += 1
        for i, ch in enumerate(s2):
            window[ord(ch) - 97] += 1
            if i >= len(s1):
                window[ord(s2[i - len(s1)]) - 97] -= 1
            if window == need:
                return True
        return False
