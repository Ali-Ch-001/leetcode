"""
664. Strange Printer
Difficulty: Hard
https://leetcode.com/problems/strange-printer/

──────────────────────────────────────────────────

There is a strange printer with the following two special properties:

• The printer can only print a sequence of the same character each
time.

• At each turn, the printer can print new characters starting from
and ending at any place and will cover the original existing
characters.

Given a string s, return the minimum number of turns the printer
needed to print it.

 

Example 1:

Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".

Example 2:

Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second
place of the string, which will cover the existing character 'a'.

 

Constraints:

	• 1 <= s.length <= 100

	• s consists of lowercase English letters.
"""

class Solution:
    def strangePrinter(self, s: str) -> int:
        compressed = []
        for ch in s:
            if not compressed or compressed[-1] != ch:
                compressed.append(ch)
        s = "".join(compressed)
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                dp[i][j] = dp[i + 1][j] + 1
                for k in range(i + 1, j + 1):
                    if s[k] == s[i]:
                        dp[i][j] = min(dp[i][j], dp[i + 1][k - 1] + dp[k][j])
        return dp[0][n - 1] if n else 0
