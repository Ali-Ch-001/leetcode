"""
1896. Minimum Cost to Change the Final Value of Expression
Difficulty: Hard
https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/

──────────────────────────────────────────────────

You are given a valid boolean expression as a string expression
consisting of the characters '1','0','&' (bitwise AND operator),'|'
(bitwise OR operator),'(', and ')'.

• For example, "()1|1" and "(1)&()" are not valid while "1",
"(((1))|(0))", and "1|(0&(1))" are valid expressions.

Return the minimum cost to change the final value of the expression.

• For example, if expression = "1|1|(0&0)&1", its value is
1|1|(0&0)&1 = 1|1|0&1 = 1|0&1 = 1&1 = 1. We want to apply operations
so that the new expression evaluates to 0.

The cost of changing the final value of an expression is the number
of operations performed on the expression. The types of operations are
described as follows:

	• Turn a '1' into a '0'.

	• Turn a '0' into a '1'.

	• Turn a '&' into a '|'.

	• Turn a '|' into a '&'.

Note: '&' does not take precedence over '|' in the order of
calculation. Evaluate parentheses first, then in left-to-right order.

 

Example 1:

Input: expression = "1&(0|1)"
Output: 1
Explanation: We can turn "1&(0|1)" into "1&(0&1)" by changing the '|'
to a '&' using 1 operation.
The new expression evaluates to 0. 

Example 2:

Input: expression = "(0&0)&(0&0&0)"
Output: 3
Explanation: We can turn "(0&0)&(0&0&0)" into "(0|1)|(0&0&0)" using 3
operations.
The new expression evaluates to 1.

Example 3:

Input: expression = "(0|(1|0&1))"
Output: 1
Explanation: We can turn "(0|(1|0&1))" into "(0|(0|0&1))" using 1
operation.
The new expression evaluates to 0.

 

Constraints:

	• 1 <= expression.length <= 10^5

	• expression only contains '1','0','&','|','(', and ')'

	• All parentheses are properly matched.

• There will be no empty parentheses (i.e: "()" is not a substring
of expression).
"""

class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        ops = []
        vals = []

        def combine(left, right, op):
            v1, d1 = left
            v2, d2 = right
            if op == '&':
                v = v1 & v2
                if v == 0:
                    m1 = 0 if v1 == 1 else d1
                    m2 = 0 if v2 == 1 else d2
                    d = min(m1 + m2, 1 + min(m1, m2))
                else:
                    m1 = 0 if v1 == 0 else d1
                    m2 = 0 if v2 == 0 else d2
                    d = min(min(m1, m2), 1 + m1 + m2)
            else:
                v = v1 | v2
                if v == 0:
                    m1 = 0 if v1 == 1 else d1
                    m2 = 0 if v2 == 1 else d2
                    d = min(min(m1, m2), 1 + m1 + m2)
                else:
                    m1 = 0 if v1 == 0 else d1
                    m2 = 0 if v2 == 0 else d2
                    d = min(m1 + m2, 1 + min(m1, m2))
            return (v, d)

        for ch in expression:
            if ch == '(':
                ops.append(ch)
            elif ch == ')':
                ops.pop()
                if ops and ops[-1] != '(':
                    op = ops.pop()
                    b = vals.pop()
                    a = vals.pop()
                    vals.append(combine(a, b, op))
            elif ch in '&|':
                ops.append(ch)
            else:
                vals.append((int(ch), 1))
                if ops and ops[-1] != '(':
                    op = ops.pop()
                    b = vals.pop()
                    a = vals.pop()
                    vals.append(combine(a, b, op))

        return vals[-1][1]
