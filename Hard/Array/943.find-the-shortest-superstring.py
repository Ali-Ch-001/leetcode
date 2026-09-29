"""
943. Find the Shortest Superstring
Difficulty: Hard
https://leetcode.com/problems/find-the-shortest-superstring/

──────────────────────────────────────────────────

Given an array of strings words, return the smallest string that
contains each string in words as a substring. If there are multiple
valid strings of the smallest length, return any of them.

You may assume that no string in words is a substring of another
string in words.

 

Example 1:

Input: words = ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex","loves","leetcode" would also
be accepted.

Example 2:

Input: words = ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"

 

Constraints:

	• 1 <= words.length <= 12

	• 1 <= words[i].length <= 20

	• words[i] consists of lowercase English letters.

	• All the strings of words are unique.
"""

from functools import lru_cache


class Solution:
    def shortestSuperstring(self, words: list[str]) -> str:
        n = len(words)
        overlap = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                limit = min(len(words[i]), len(words[j]))
                for length in range(limit, 0, -1):
                    if words[i].endswith(words[j][:length]):
                        overlap[i][j] = length
                        break
        full = (1 << n) - 1

        @lru_cache(maxsize=None)
        def dfs(mask, last):
            if mask == full:
                return words[last]
            best = None
            for nxt in range(n):
                if mask & (1 << nxt):
                    continue
                tail = dfs(mask | (1 << nxt), nxt)
                candidate = words[last] + tail[overlap[last][nxt]:]
                if best is None or len(candidate) < len(best):
                    best = candidate
            return best

        result = None
        for start in range(n):
            candidate = dfs(1 << start, start)
            if result is None or len(candidate) < len(result):
                result = candidate
        return result
