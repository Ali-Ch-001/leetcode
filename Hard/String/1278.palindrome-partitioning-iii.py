"""
1278. Palindrome Partitioning III
Difficulty: Hard
https://leetcode.com/problems/palindrome-partitioning-iii/

──────────────────────────────────────────────────

You are given a string s containing lowercase letters and an integer
k. You need to :

• First, change some characters of s to other lowercase English
letters.

• Then divide s into k non-empty disjoint substrings such that each
substring is a palindrome.

Return the minimal number of characters that you need to change to
divide the string.

 

Example 1:

Input: s = "abc", k = 2
Output: 1
Explanation: You can split the string into "ab" and "c", and change 1
character in "ab" to make it palindrome.

Example 2:

Input: s = "aabbc", k = 3
Output: 0
Explanation: You can split the string into "aa", "bb" and "c", all of
them are palindrome.

Example 3:

Input: s = "leetcode", k = 8
Output: 0

 

Constraints:

	• 1 <= k <= s.length <= 100.

	• s only contains lowercase English letters.
"""

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                cost[i][j] = cost[i + 1][j - 1] + (s[i] != s[j])

        dp = [cost[0][j] for j in range(n)]
        for _ in range(2, k + 1):
            ndp = [float('inf')] * n
            for j in range(1, n):
                best = float('inf')
                for i in range(1, j + 1):
                    v = dp[i - 1] + cost[i][j]
                    if v < best:
                        best = v
                ndp[j] = best
            dp = ndp
        return dp[n - 1]
