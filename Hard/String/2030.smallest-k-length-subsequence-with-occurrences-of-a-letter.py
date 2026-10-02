"""
2030. Smallest K-Length Subsequence With Occurrences of a Letter
Difficulty: Hard
https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/

──────────────────────────────────────────────────

You are given a string s, an integer k, a letter letter, and an
integer repetition.

Return the lexicographically smallest subsequence of s of length k
that has the letter letter appear at least repetition times. The test
cases are generated so that the letter appears in s at least
repetition times.

A subsequence is a string that can be derived from another string by
deleting some or no characters without changing the order of the
remaining characters.

A string a is lexicographically smaller than a string b if in the
first position where a and b differ, string a has a letter that
appears earlier in the alphabet than the corresponding letter in b.

 

Example 1:

Input: s = "leet", k = 3, letter = "e", repetition = 1
Output: "eet"
Explanation: There are four subsequences of length 3 that have the
letter 'e' appear at least 1 time:
- "lee" (from "leet")
- "let" (from "leet")
- "let" (from "leet")
- "eet" (from "leet")
The lexicographically smallest subsequence among them is "eet".

Example 2:

Input: s = "leetcode", k = 4, letter = "e", repetition = 2
Output: "ecde"
Explanation: "ecde" is the lexicographically smallest subsequence of
length 4 that has the letter "e" appear at least 2 times.

Example 3:

Input: s = "bb", k = 2, letter = "b", repetition = 2
Output: "bb"
Explanation: "bb" is the only subsequence of length 2 that has the
letter "b" appear at least 2 times.

 

Constraints:

	• 1 <= repetition <= k <= s.length <= 5 * 10^4

	• s consists of lowercase English letters.

• letter is a lowercase English letter, and appears in s at least
repetition times.
"""

from bisect import bisect_left


class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        n = len(s)
        positions = {}
        for i, c in enumerate(s):
            positions.setdefault(c, []).append(i)

        suffix_letter = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_letter[i] = suffix_letter[i + 1] + (1 if s[i] == letter else 0)

        res = []
        start = 0
        need_len = k
        need_letter = repetition
        while need_len > 0:
            max_p = n - need_len
            for code in range(26):
                ch = chr(97 + code)
                lst = positions.get(ch)
                if not lst:
                    continue
                idx = bisect_left(lst, start)
                if idx == len(lst):
                    continue
                p = lst[idx]
                if p > max_p:
                    continue
                needed_after = need_letter - (1 if ch == letter else 0)
                if needed_after > suffix_letter[p + 1]:
                    continue
                if needed_after > need_len - 1:
                    continue
                res.append(ch)
                start = p + 1
                need_len -= 1
                if ch == letter:
                    need_letter -= 1
                break
            else:
                break
        return ''.join(res)
