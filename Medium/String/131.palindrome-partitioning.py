"""
131. Palindrome Partitioning
Difficulty: Medium
https://leetcode.com/problems/palindrome-partitioning/

──────────────────────────────────────────────────

Given a string s, partition s such that every substring of the
partition is a palindrome. Return all possible palindrome partitioning
of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]

 

Constraints:

	• 1 <= s.length <= 16

	• s contains only lowercase English letters.
"""

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        results = []

        def backtrack(start: int, path: list[str]) -> None:
            if start == len(s):
                results.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                piece = s[start:end]
                if piece == piece[::-1]:
                    path.append(piece)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return results
