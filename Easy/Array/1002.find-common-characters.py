"""
1002. Find Common Characters
Difficulty: Easy
https://leetcode.com/problems/find-common-characters/

──────────────────────────────────────────────────

Given a string array words, return an array of all characters that
show up in all strings within the words (including duplicates). You
may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]

 

Constraints:

	• 1 <= words.length <= 100

	• 1 <= words[i].length <= 100

	• words[i] consists of lowercase English letters.
"""

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        common = None
        for word in words:
            counts = {}
            for ch in word:
                counts[ch] = counts.get(ch, 0) + 1
            if common is None:
                common = counts
            else:
                for ch in list(common):
                    if ch in counts:
                        common[ch] = min(common[ch], counts[ch])
                    else:
                        del common[ch]
        result = []
        for ch, count in common.items():
            result.extend([ch] * count)
        return result
