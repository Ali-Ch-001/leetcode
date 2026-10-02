"""
1888. Minimum Number of Flips to Make the Binary String Alternating
Difficulty: Medium
https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

──────────────────────────────────────────────────

You are given a binary string s. You are allowed to perform two types
of operations on the string in any sequence:

• Type-1: Remove the character at the start of the string s and
append it to the end of the string.

• Type-2: Pick any character in s and flip its value, i.e., if its
value is '0' it becomes '1' and vice-versa.

Return the minimum number of type-2 operations you need to perform
such that s becomes alternating.

The string is called alternating if no two adjacent characters are
equal.

• For example, the strings "010" and "1010" are alternating, while
the string "0100" is not.

 

Example 1:

Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to
make s = "101010".

Example 2:

Input: s = "010"
Output: 0
Explanation: The string is already alternating.

Example 3:

Input: s = "1110"
Output: 1
Explanation: Use the second operation on the second element to make s
= "1010".

 

Constraints:

	• 1 <= s.length <= 10^5

	• s[i] is either '0' or '1'.
"""

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        doubled = s + s
        pref0 = [0] * (2 * n + 1)
        pref1 = [0] * (2 * n + 1)
        for i, ch in enumerate(doubled):
            exp0 = '0' if i % 2 == 0 else '1'
            pref0[i + 1] = pref0[i] + (ch != exp0)
            pref1[i + 1] = pref1[i] + (ch == exp0)
        best = n
        for start in range(n):
            c0 = pref0[start + n] - pref0[start]
            c1 = pref1[start + n] - pref1[start]
            if c0 < best:
                best = c0
            if c1 < best:
                best = c1
        return best

