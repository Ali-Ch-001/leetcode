"""
132. Palindrome Partitioning II
Difficulty: Hard
https://leetcode.com/problems/palindrome-partitioning-ii/

──────────────────────────────────────────────────

Given a string s, partition s such that every substring of the
partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced
using 1 cut.

Example 2:

Input: s = "a"
Output: 0

Example 3:

Input: s = "ab"
Output: 1

 

Constraints:

	• 1 <= s.length <= 2000

	• s consists of lowercase English letters only.
"""

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True
        dp = [0] * (n + 1)
        for end in range(1, n + 1):
            best = end - 1
            for start in range(end):
                if is_pal[start][end - 1]:
                    if start == 0:
                        best = 0
                        break
                    best = min(best, dp[start] + 1)
            dp[end] = best
        return dp[n]
