"""
289. Game of Life
Difficulty: Medium
https://leetcode.com/problems/game-of-life/

──────────────────────────────────────────────────

According to Wikipedia's article: "The Game of Life, also known
simply as Life, is a cellular automaton devised by the British
mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has
an initial state: live (represented by a 1) or dead (represented by a
0). Each cell interacts with its eight neighbors (horizontal,
vertical, diagonal) using the following four rules (taken from the
above Wikipedia article):

• Any live cell with fewer than two live neighbors dies as if caused
by under-population.

• Any live cell with two or three live neighbors lives on to the
next generation.

• Any live cell with more than three live neighbors dies, as if by
over-population.

• Any dead cell with exactly three live neighbors becomes a live
cell, as if by reproduction.

The next state of the board is determined by applying the above rules
simultaneously to every cell in the current state of the m x n grid
board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its
next state.

Note that you do not need to return anything.

 

Example 1:

Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:

Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]

 

Constraints:

	• m == board.length

	• n == board[i].length

	• 1 <= m, n <= 25

	• board[i][j] is 0 or 1.

 

Follow up:

• Could you solve it in-place? Remember that the board needs to be
updated simultaneously: You cannot update some cells first and then
use their updated values to update other cells.

• In this question, we represent the board using a 2D array. In
principle, the board is infinite, which would cause problems when the
active area encroaches upon the border of the array (i.e., live cells
reach the border). How would you address these problems?
"""

class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                live = 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in (1, 3):
                            live += 1
                if board[r][c] == 1:
                    if live < 2 or live > 3:
                        board[r][c] = 3
                elif live == 3:
                    board[r][c] = 2
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 3:
                    board[r][c] = 0
                elif board[r][c] == 2:
                    board[r][c] = 1
