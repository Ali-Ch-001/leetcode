"""
438. Find All Anagrams in a String
Difficulty: Medium
https://leetcode.com/problems/find-all-anagrams-in-a-string/

──────────────────────────────────────────────────

Given two strings s and p, return an array of all the start indices
of p's anagrams in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of
"abc".
The substring with start index = 6 is "bac", which is an anagram of
"abc".

Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of
"ab".
The substring with start index = 1 is "ba", which is an anagram of
"ab".
The substring with start index = 2 is "ab", which is an anagram of
"ab".

 

Constraints:

	• 1 <= s.length, p.length <= 3 * 10^4

	• s and p consist of lowercase English letters.
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []
        need = {}
        for ch in p:
            need[ch] = need.get(ch, 0) + 1
        window = {}
        for ch in s[:len(p)]:
            window[ch] = window.get(ch, 0) + 1
        result = []
        if window == need:
            result.append(0)
        for i in range(len(p), len(s)):
            outgoing = s[i - len(p)]
            window[outgoing] -= 1
            if window[outgoing] == 0:
                del window[outgoing]
            incoming = s[i]
            window[incoming] = window.get(incoming, 0) + 1
            if window == need:
                result.append(i - len(p) + 1)
        return result
