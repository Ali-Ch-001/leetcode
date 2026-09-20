"""
44. Wildcard Matching
Difficulty: Hard
https://leetcode.com/problems/wildcard-matching/

──────────────────────────────────────────────────

Given an input string (s) and a pattern (p), implement wildcard
pattern matching with support for '?' and '*' where:

	• '?' Matches any single character.

• '*' Matches any sequence of characters (including the empty
sequence).

The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which
does not match 'b'.

 

Constraints:

	• 0 <= s.length, p.length <= 2000

	• s contains only lowercase English letters.

	• p contains only lowercase English letters, '?' or '*'.
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_index = p_index = 0
        star_index = match_index = -1
        while s_index < len(s):
            if p_index < len(p) and (p[p_index] == "?" or p[p_index] == s[s_index]):
                s_index += 1
                p_index += 1
            elif p_index < len(p) and p[p_index] == "*":
                star_index = p_index
                match_index = s_index
                p_index += 1
            elif star_index != -1:
                p_index = star_index + 1
                match_index += 1
                s_index = match_index
            else:
                return False
        while p_index < len(p) and p[p_index] == "*":
            p_index += 1
        return p_index == len(p)
