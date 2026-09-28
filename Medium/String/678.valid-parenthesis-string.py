"""
678. Valid Parenthesis String
Difficulty: Medium
https://leetcode.com/problems/valid-parenthesis-string/

──────────────────────────────────────────────────

Given a string s containing only three types of characters: '(', ')'
and '*', return true if s is valid.

The following rules define a valid string:

• Any left parenthesis '(' must have a corresponding right
parenthesis ')'.

• Any right parenthesis ')' must have a corresponding left
parenthesis '('.

• Left parenthesis '(' must go before the corresponding right
parenthesis ')'.

• '*' could be treated as a single right parenthesis ')' or a single
left parenthesis '(' or an empty string "".

 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "(*)"
Output: true

Example 3:

Input: s = "(*))"
Output: true

Example 4:

Input: s = "("
Output: false

 

Constraints:

	• 1 <= s.length <= 100

	• s[i] is '(', ')' or '*'.
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0
        for ch in s:
            if ch == "(":
                low += 1
                high += 1
            elif ch == ")":
                low = max(low - 1, 0)
                high -= 1
            else:
                low = max(low - 1, 0)
                high += 1
            if high < 0:
                return False
        return low == 0
