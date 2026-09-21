"""
409. Longest Palindrome
Difficulty: Easy
https://leetcode.com/problems/longest-palindrome/

──────────────────────────────────────────────────

Given a string s which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with
those letters.

Letters are case sensitive, for example, "Aa" is not considered a
palindrome.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd",
whose length is 7.

Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose
length is 1.

 

Constraints:

	• 1 <= s.length <= 2000

	• s consists of lowercase and/or uppercase English letters only.
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        length = 0
        odd = False
        for count in counts.values():
            length += count // 2 * 2
            if count % 2:
                odd = True
        return length + 1 if odd else length
