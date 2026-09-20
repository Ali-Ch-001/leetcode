"""
52. N-Queens II
Difficulty: Hard
https://leetcode.com/problems/n-queens-ii/

──────────────────────────────────────────────────

The n-queens puzzle is the problem of placing n queens on an n x n
chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the
n-queens puzzle.

 

Example 1:

Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle
as shown.

Example 2:

Input: n = 1
Output: 1

 

Constraints:

	• 1 <= n <= 9
"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(r: int) -> None:
            nonlocal count
            if r == n:
                count += 1
                return
            for c in range(n):
                if c in cols or (r + c) in diag1 or (r - c) in diag2:
                    continue
                cols.add(c)
                diag1.add(r + c)
                diag2.add(r - c)
                backtrack(r + 1)
                cols.remove(c)
                diag1.remove(r + c)
                diag2.remove(r - c)

        backtrack(0)
        return count
