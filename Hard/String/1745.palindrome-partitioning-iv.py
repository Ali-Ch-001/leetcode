"""
1745. Palindrome Partitioning IV
Difficulty: Hard
https://leetcode.com/problems/palindrome-partitioning-iv/

──────────────────────────────────────────────────

Given a string s, return true if it is possible to split the string s
into three non-empty palindromic substrings. Otherwise, return
false.​​​​​

A string is said to be palindrome if it the same string when reversed.

 

Example 1:

Input: s = "abcbdd"
Output: true
Explanation: "abcbdd" = "a" + "bcb" + "dd", and all three substrings
are palindromes.

Example 2:

Input: s = "bcbddxy"
Output: false
Explanation: s cannot be split into 3 palindromes.

 

Constraints:

	• 3 <= s.length <= 2000

	• s​​​​​​ consists only of lowercase English letters.
"""

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        char_mask = [0] * 26
        for j, ch in enumerate(s):
            char_mask[ord(ch) - 97] |= 1 << j
        pal = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            mask = (1 << i) | (char_mask[ord(s[i]) - 97] & (pal[i + 1] << 1))
            if i + 1 < n and s[i] == s[i + 1]:
                mask |= 1 << (i + 1)
            pal[i] = mask
        end_ok = 0
        for j in range(n - 2, -1, -1):
            if (pal[j + 1] >> (n - 1)) & 1:
                end_ok |= 1 << j
        for i in range(n - 2):
            if (pal[0] >> i) & 1 and (pal[i + 1] & end_ok):
                return True
        return False
