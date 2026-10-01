"""
1542. Find Longest Awesome Substring
Difficulty: Hard
https://leetcode.com/problems/find-longest-awesome-substring/

──────────────────────────────────────────────────

You are given a string s. An awesome substring is a non-empty
substring of s such that we can make any number of swaps in order to
make it a palindrome.

Return the length of the maximum length awesome substring of s.

 

Example 1:

Input: s = "3242415"
Output: 5
Explanation: "24241" is the longest awesome substring, we can form
the palindrome "24142" with some swaps.

Example 2:

Input: s = "12345678"
Output: 1

Example 3:

Input: s = "213123"
Output: 6
Explanation: "213123" is the longest awesome substring, we can form
the palindrome "231132" with some swaps.

 

Constraints:

	• 1 <= s.length <= 10^5

	• s consists only of digits.
"""

class Solution:
    def longestAwesome(self, s: str) -> int:
        first = {0: -1}
        mask = 0
        ans = 0
        for i, ch in enumerate(s):
            mask ^= 1 << (ord(ch) - 48)
            if mask in first:
                if i - first[mask] > ans:
                    ans = i - first[mask]
            else:
                first[mask] = i
            for b in range(10):
                m2 = mask ^ (1 << b)
                if m2 in first and i - first[m2] > ans:
                    ans = i - first[m2]
        return ans

