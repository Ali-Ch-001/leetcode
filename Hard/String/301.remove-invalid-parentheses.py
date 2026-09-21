"""
301. Remove Invalid Parentheses
Difficulty: Hard
https://leetcode.com/problems/remove-invalid-parentheses/

──────────────────────────────────────────────────

Given a string s that contains parentheses and letters, remove the
minimum number of invalid parentheses to make the input string valid.

Return a list of unique strings that are valid with the minimum
number of removals. You may return the answer in any order.

 

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]

Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Example 3:

Input: s = ")("
Output: [""]

 

Constraints:

	• 1 <= s.length <= 25

• s consists of lowercase English letters and parentheses '(' and
')'.

	• There will be at most 20 parentheses in s.
"""

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def valid(text: str) -> bool:
            balance = 0
            for ch in text:
                if ch == "(":
                    balance += 1
                elif ch == ")":
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0

        level = {s}
        while True:
            found = [text for text in level if valid(text)]
            if found:
                return found
            next_level = set()
            for text in level:
                for i in range(len(text)):
                    if text[i] in "()":
                        next_level.add(text[:i] + text[i + 1:])
            level = next_level
