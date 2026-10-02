"""
1960. Maximum Product of the Length of Two Palindromic Substrings
Difficulty: Hard
https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/

──────────────────────────────────────────────────

You are given a 0-indexed string s and are tasked with finding two
non-intersecting palindromic substrings of odd length such that the
product of their lengths is maximized.

More formally, you want to choose four integers i, j, k, l such that
0 <= i <= j < k <= l < s.length and both the substrings s[i...j] and
s[k...l] are palindromes and have odd lengths. s[i...j] denotes a
substring from index i to index j inclusive.

Return the maximum possible product of the lengths of the two
non-intersecting palindromic substrings.

A palindrome is a string that is the same forward and backward. A
substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "ababbb"
Output: 9
Explanation: Substrings "aba" and "bbb" are palindromes with odd
length. product = 3 * 3 = 9.

Example 2:

Input: s = "zaaaxbbby"
Output: 9
Explanation: Substrings "aaa" and "bbb" are palindromes with odd
length. product = 3 * 3 = 9.

 

Constraints:

	• 2 <= s.length <= 10^5

	• s consists of lowercase English letters.
"""

class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        d1 = [0] * n
        l, r = 0, -1
        for i in range(n):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)
            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                k += 1
            d1[i] = k
            if i + k - 1 > r:
                l = i - k + 1
                r = i + k - 1

        best1 = [0] * n
        best2 = [0] * n
        for i in range(n):
            length = 2 * d1[i] - 1
            end = i + d1[i] - 1
            if length > best1[end]:
                best1[end] = length
            start = i - d1[i] + 1
            if length > best2[start]:
                best2[start] = length
        for i in range(1, n):
            if best1[i - 1] > best1[i]:
                best1[i] = best1[i - 1]
        for i in range(n - 2, -1, -1):
            if best2[i + 1] > best2[i]:
                best2[i] = best2[i + 1]

        ans = 0
        for i in range(n - 1):
            ans = max(ans, best1[i] * best2[i + 1])
        return ans

