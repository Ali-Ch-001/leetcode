"""
472. Concatenated Words
Difficulty: Hard
https://leetcode.com/problems/concatenated-words/

──────────────────────────────────────────────────

Given an array of strings words (without duplicates), return all the
concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely
of at least two shorter words (not necessarily distinct) in the given
array.

 

Example 1:

Input: words =
["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and
"cats";
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Example 2:

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]

 

Constraints:

	• 1 <= words.length <= 10^4

	• 1 <= words[i].length <= 30

	• words[i] consists of only lowercase English letters.

	• All the strings of words are unique.

	• 1 <= sum(words[i].length) <= 10^5
"""

class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        word_set = set(words)

        def can_form(word: str) -> bool:
            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True
            for end in range(1, n + 1):
                for start in range(end):
                    if dp[start] and end - start < n and word[start:end] in word_set:
                        dp[end] = True
                        break
            return dp[n]

        return [word for word in words if can_form(word)]
