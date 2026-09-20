"""
130. Surrounded Regions
Difficulty: Medium
https://leetcode.com/problems/surrounded-regions/

──────────────────────────────────────────────────

You are given an m x n matrix board containing letters 'X' and 'O',
capture regions that are surrounded:

• Connect: A cell is connected to adjacent cells horizontally or
vertically.

	• Region: To form a region connect every 'O' cell.

• Surround: A region is surrounded if none of the 'O' cells in that
region are on the edge of the board. Such regions are completely
enclosed by 'X' cells.

To capture a surrounded region, replace all 'O's with 'X's in-place
within the original board. You do not need to return anything.

 

Example 1:

Input: board =
[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output:
[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:

In the above diagram, the bottom region is not captured because it is
on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]

 

Constraints:

	• m == board.length

	• n == board[i].length

	• 1 <= m, n <= 200

	• board[i][j] is 'X' or 'O'.
"""

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        if not board:
            return
        rows, cols = len(board), len(board[0])
        stack = []
        for r in range(rows):
            for c in range(cols):
                if (r in (0, rows - 1) or c in (0, cols - 1)) and board[r][c] == "O":
                    stack.append((r, c))
        while stack:
            r, c = stack.pop()
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != "O":
                continue
            board[r][c] = "#"
            stack.extend([(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)])
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
