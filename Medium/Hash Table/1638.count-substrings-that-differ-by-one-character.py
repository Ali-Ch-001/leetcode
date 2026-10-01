"""
1638. Count Substrings That Differ by One Character
Difficulty: Medium
https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

──────────────────────────────────────────────────

Given two strings s and t, find the number of ways you can choose a
non-empty substring of s and replace a single character by a different
character such that the resulting substring is a substring of t. In
other words, find the number of substrings in s that differ from some
substring in t by exactly one character.

For example, the underlined substrings in "computer" and
"computation" only differ by the 'e'/'a', so this is a valid way.

Return the number of substrings that satisfy the condition above.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "aba", t = "baba"
Output: 6
Explanation: The following are the pairs of substrings from s and t
that differ by exactly 1 character:
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
The underlined portions are the substrings that are chosen from s and
t.

​​
Example 2:

Input: s = "ab", t = "bb"
Output: 3
Explanation: The following are the pairs of substrings from s and t
that differ by 1 character:
("ab", "bb")
("ab", "bb")
("ab", "bb")
​​​​The underlined portions are the substrings that are chosen from s
and t.

 

Constraints:

	• 1 <= s.length, t.length <= 100

	• s and t consist of lowercase English letters only.
"""

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        lcp = [[0] * (m + 1) for _ in range(n + 1)]
        rcp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    lcp[i][j] = lcp[i - 1][j - 1] + 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s[i] == t[j]:
                    rcp[i][j] = rcp[i + 1][j + 1] + 1
        ans = 0
        for i in range(n):
            for j in range(m):
                if s[i] != t[j]:
                    ans += (lcp[i][j] + 1) * (rcp[i + 1][j + 1] + 1)
        return ans
        
