"""
22. Generate Parentheses
Difficulty: Medium
https://leetcode.com/problems/generate-parentheses/

──────────────────────────────────────────────────

Given n pairs of parentheses, write a function to generate all
combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

 

Constraints:

	• 1 <= n <= 8
"""

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current: str, opened: int, closed: int) -> None:
            if len(current) == 2 * n:
                result.append(current)
                return
            if opened < n:
                backtrack(current + "(", opened + 1, closed)
            if closed < opened:
                backtrack(current + ")", opened, closed + 1)

        backtrack("", 0, 0)
        return result
