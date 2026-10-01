"""
1444. Number of Ways of Cutting a Pizza
Difficulty: Hard
https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/

──────────────────────────────────────────────────

Given a rectangular pizza represented as a rows x cols matrix
containing the following characters: 'A' (an apple) and '.' (empty
cell) and given the integer k. You have to cut the pizza into k pieces
using k-1 cuts.

For each cut you choose the direction: vertical or horizontal, then
you choose a cut position at the cell boundary and cut the pizza into
two pieces. If you cut the pizza vertically, give the left part of the
pizza to a person. If you cut the pizza horizontally, give the upper
part of the pizza to a person. Give the last piece of pizza to the
last person.

Return the number of ways of cutting the pizza such that each piece
contains at least one apple. Since the answer can be a huge number,
return this modulo 10^9 + 7.

 

Example 1:

Input: pizza = ["A..","AAA","..."], k = 3
Output: 3 
Explanation: The figure above shows the three ways to cut the pizza.
Note that pieces must contain at least one apple.

Example 2:

Input: pizza = ["A..","AA.","..."], k = 3
Output: 1

Example 3:

Input: pizza = ["A..","A..","..."], k = 1
Output: 1

 

Constraints:

	• 1 <= rows, cols <= 50

	• rows == pizza.length

	• cols == pizza[i].length

	• 1 <= k <= 10

	• pizza consists of characters 'A' and '.' only.
"""

class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        from functools import lru_cache
        MOD = 10**9 + 7
        rows = len(pizza)
        cols = len(pizza[0])
        pre = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(rows):
            for j in range(cols):
                pre[i + 1][j + 1] = (pre[i][j + 1] + pre[i + 1][j] - pre[i][j]
                                     + (1 if pizza[i][j] == 'A' else 0))

        def apples(r1, c1, r2, c2):
            return pre[r2][c2] - pre[r1][c2] - pre[r2][c1] + pre[r1][c1]

        @lru_cache(maxsize=None)
        def solve(r, c, pieces):
            if apples(r, c, rows, cols) == 0:
                return 0
            if pieces == 1:
                return 1
            total = 0
            for r2 in range(r + 1, rows):
                if apples(r, c, r2, cols) > 0:
                    total += solve(r2, c, pieces - 1)
            for c2 in range(c + 1, cols):
                if apples(r, c, rows, c2) > 0:
                    total += solve(r, c2, pieces - 1)
            return total % MOD

        return solve(0, 0, k)
