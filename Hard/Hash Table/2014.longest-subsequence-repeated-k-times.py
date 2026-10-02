"""
2014. Longest Subsequence Repeated k Times
Difficulty: Hard
https://leetcode.com/problems/longest-subsequence-repeated-k-times/

──────────────────────────────────────────────────

You are given a string s of length n, and an integer k. You are
tasked to find the longest subsequence repeated k times in string s.

A subsequence is a string that can be derived from another string by
deleting some or no characters without changing the order of the
remaining characters.

A subsequence seq is repeated k times in the string s if seq * k is a
subsequence of s, where seq * k represents a string constructed by
concatenating seq k times.

• For example, "bba" is repeated 2 times in the string "bababcba",
because the string "bbabba", constructed by concatenating "bba" 2
times, is a subsequence of the string "bababcba".

Return the longest subsequence repeated k times in string s. If
multiple such subsequences are found, return the lexicographically
largest one. If there is no such subsequence, return an empty string.

 

Example 1:

Input: s = "letsleetcode", k = 2
Output: "let"
Explanation: There are two longest subsequences repeated 2 times:
"let" and "ete".
"let" is the lexicographically largest one.

Example 2:

Input: s = "bb", k = 2
Output: "b"
Explanation: The longest subsequence repeated 2 times is "b".

Example 3:

Input: s = "ab", k = 2
Output: ""
Explanation: There is no subsequence repeated 2 times. Empty string
is returned.

 

Constraints:

	• n == s.length

	• 2 <= k <= 2000

	• 2 <= n < min(2001, k * 8)

	• s consists of lowercase English letters.
"""

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)
        freq = [0] * 26
        for c in s:
            freq[ord(c) - 97] += 1
        allowed = [chr(97 + i) for i in range(25, -1, -1) if freq[i] >= k]
        if not allowed:
            return ""

        nxt = [[n] * 26 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            row = nxt[i + 1][:]
            row[ord(s[i]) - 97] = i
            nxt[i] = row

        def is_rep(seq):
            pos = 0
            for _ in range(k):
                for c in seq:
                    idx = nxt[pos][ord(c) - 97]
                    if idx == n:
                        return False
                    pos = idx + 1
            return True

        max_len = n // k
        current = [""]
        answer = ""
        for _ in range(max_len):
            nxt_level = []
            for prefix in current:
                for c in allowed:
                    cand = prefix + c
                    if is_rep(cand):
                        nxt_level.append(cand)
            if not nxt_level:
                break
            answer = max(nxt_level)
            current = nxt_level
        return answer
