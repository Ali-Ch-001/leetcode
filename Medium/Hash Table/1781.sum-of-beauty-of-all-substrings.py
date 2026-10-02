"""
1781. Sum of Beauty of All Substrings
Difficulty: Medium
https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

──────────────────────────────────────────────────

The beauty of a string is the difference in frequencies between the
most frequent and least frequent characters.

	• For example, the beauty of "abaacc" is 3 - 1 = 2.

Given a string s, return the sum of beauty of all of its substrings.

 

Example 1:

Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are
["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.

Example 2:

Input: s = "aabcbaa"
Output: 17

 

Constraints:

	• 1 <= s.length <=^ 500

	• s consists of only lowercase English letters.
"""

class Solution:
    def beautySum(self, s: str) -> int:
        total = 0
        n = len(s)
        for i in range(n):
            cnt = [0] * 26
            for j in range(i, n):
                cnt[ord(s[j]) - 97] += 1
                freqs = [c for c in cnt if c]
                total += max(freqs) - min(freqs)
        return total
