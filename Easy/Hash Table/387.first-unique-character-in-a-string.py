"""
387. First Unique Character in a String
Difficulty: Easy
https://leetcode.com/problems/first-unique-character-in-a-string/

──────────────────────────────────────────────────

Given a string s, find the first non-repeating character in it and
return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not
occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1

 

Constraints:

	• 1 <= s.length <= 10^5

	• s consists of only lowercase English letters.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        for i, ch in enumerate(s):
            if counts[ch] == 1:
                return i
        return -1
