"""
854. K-Similar Strings
Difficulty: Hard
https://leetcode.com/problems/k-similar-strings/

──────────────────────────────────────────────────

Strings s1 and s2 are k-similar (for some non-negative integer k) if
we can swap the positions of two letters in s1 exactly k times so that
the resulting string equals s2.

Given two anagrams s1 and s2, return the smallest k for which s1 and
s2 are k-similar.

 

Example 1:

Input: s1 = "ab", s2 = "ba"
Output: 1
Explanation: The two string are 1-similar because we can use one swap
to change s1 to s2: "ab" --> "ba".

Example 2:

Input: s1 = "abc", s2 = "bca"
Output: 2
Explanation: The two strings are 2-similar because we can use two
swaps to change s1 to s2: "abc" --> "bac" --> "bca".

 

Constraints:

	• 1 <= s1.length <= 20

	• s2.length == s1.length

• s1 and s2 contain only lowercase letters from the set {'a', 'b',
'c', 'd', 'e', 'f'}.

	• s2 is an anagram of s1.
"""

from collections import deque


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        queue = deque([(s1, 0)])
        visited = {s1}
        while queue:
            current, swaps = queue.popleft()
            index = 0
            while current[index] == s2[index]:
                index += 1
            for j in range(index + 1, len(s1)):
                if current[j] == s2[index] and current[j] != s2[j]:
                    nxt = (
                        current[:index]
                        + current[j]
                        + current[index + 1:j]
                        + current[index]
                        + current[j + 1:]
                    )
                    if nxt == s2:
                        return swaps + 1
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, swaps + 1))
        return -1
