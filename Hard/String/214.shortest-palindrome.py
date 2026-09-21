"""
214. Shortest Palindrome
Difficulty: Hard
https://leetcode.com/problems/shortest-palindrome/

──────────────────────────────────────────────────

You are given a string s. You can convert s to a palindrome by adding
characters in front of it.

Return the shortest palindrome you can find by performing this
transformation.

 

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"

Example 2:

Input: s = "abcd"
Output: "dcbabcd"

 

Constraints:

	• 0 <= s.length <= 5 * 10^4

	• s consists of lowercase English letters only.
"""

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        combined = s + "#" + s[::-1]
        pi = [0] * len(combined)
        for i in range(1, len(combined)):
            j = pi[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = pi[j - 1]
            if combined[i] == combined[j]:
                j += 1
            pi[i] = j
        longest = pi[-1]
        return s[longest:][::-1] + s
