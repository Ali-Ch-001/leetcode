"""
1593. Split a String Into the Max Number of Unique Substrings
Difficulty: Medium
https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

──────────────────────────────────────────────────

Given a string s, return the maximum number of unique substrings that
the given string can be split into.

You can split string s into any list of non-empty substrings, where
the concatenation of the substrings forms the original string.
However, you must split the substrings such that all of them are
unique.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c',
'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as
you have 'a' and 'b' multiple times.

Example 2:

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].

Example 3:

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.

 

Constraints:

	• 
	1 <= s.length <= 16

	

	• 
	s contains only lower case English letters.
"""

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        best = 0

        def dfs(i: int, count: int) -> None:
            nonlocal best
            if i == len(s):
                best = max(best, count)
                return
            if count + (len(s) - i) <= best:
                return
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]
                if sub not in seen:
                    seen.add(sub)
                    dfs(j, count + 1)
                    seen.remove(sub)

        dfs(0, 0)
        return best
