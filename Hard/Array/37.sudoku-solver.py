"""
37. Sudoku Solver
Difficulty: Hard
https://leetcode.com/problems/sudoku-solver/

──────────────────────────────────────────────────

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

	• Each of the digits 1-9 must occur exactly once in each row.

	• Each of the digits 1-9 must occur exactly once in each column.

• Each of the digits 1-9 must occur exactly once in each of the 9
3x3 sub-boxes of the grid.

The '.' character indicates empty cells.

 

Example 1:

Input: board =
[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output:
[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid
solution is shown below:

 

Constraints:

	• board.length == 9

	• board[i].length == 9

	• board[i][j] is a digit or '.'.

	• It is guaranteed that the input board has only one solution.
"""

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    empty.append((r, c))
                else:
                    box = (r // 3) * 3 + c // 3
                    rows[r].add(value)
                    cols[c].add(value)
                    boxes[box].add(value)

        def backtrack(index: int) -> bool:
            if index == len(empty):
                return True
            r, c = empty[index]
            box = (r // 3) * 3 + c // 3
            for digit in "123456789":
                if digit in rows[r] or digit in cols[c] or digit in boxes[box]:
                    continue
                board[r][c] = digit
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[box].add(digit)
                if backtrack(index + 1):
                    return True
                board[r][c] = "."
                rows[r].remove(digit)
                cols[c].remove(digit)
                boxes[box].remove(digit)
            return False

        backtrack(0)
