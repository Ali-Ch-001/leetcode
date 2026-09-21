"""
383. Ransom Note
Difficulty: Easy
https://leetcode.com/problems/ransom-note/

──────────────────────────────────────────────────

Given two strings ransomNote and magazine, return true if ransomNote
can be constructed by using the letters from magazine and false
otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

 

Constraints:

	• 1 <= ransomNote.length, magazine.length <= 10^5

	• ransomNote and magazine consist of lowercase English letters.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = {}
        for ch in magazine:
            counts[ch] = counts.get(ch, 0) + 1
        for ch in ransomNote:
            if counts.get(ch, 0) == 0:
                return False
            counts[ch] -= 1
        return True
