"""
640. Solve the Equation
Difficulty: Medium
https://leetcode.com/problems/solve-the-equation/

──────────────────────────────────────────────────

Solve a given equation and return the value of 'x' in the form of a
string "x=#value". The equation contains only '+', '-' operation, the
variable 'x' and its coefficient. You should return "No solution" if
there is no solution for the equation, or "Infinite solutions" if
there are infinite solutions for the equation.

If there is exactly one solution for the equation, we ensure that the
value of 'x' is an integer.

 

Example 1:

Input: equation = "x+5-3+x=6+x-2"
Output: "x=2"

Example 2:

Input: equation = "x=x"
Output: "Infinite solutions"

Example 3:

Input: equation = "2x=x"
Output: "x=0"

 

Constraints:

	• 3 <= equation.length <= 1000

	• equation has exactly one '='.

• equation consists of integers with an absolute value in the range
[0, 100] without any leading zeros, and the variable 'x'.

• The input is generated that if there is a single solution, it will
be an integer.
"""

class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split("=")

        def parse(side):
            coef = 0
            const = 0
            i = 0
            n = len(side)
            sign = 1
            while i < n:
                if side[i] == "+":
                    sign = 1
                    i += 1
                elif side[i] == "-":
                    sign = -1
                    i += 1
                elif side[i] == "x":
                    coef += sign
                    i += 1
                else:
                    j = i
                    while j < n and side[j].isdigit():
                        j += 1
                    number = int(side[i:j])
                    if j < n and side[j] == "x":
                        coef += sign * number
                        j += 1
                    else:
                        const += sign * number
                    i = j
            return coef, const

        lc, lconst = parse(left)
        rc, rconst = parse(right)
        coef = lc - rc
        const = rconst - lconst
        if coef == 0:
            return "No solution" if const != 0 else "Infinite solutions"
        return f"x={const // coef}"
