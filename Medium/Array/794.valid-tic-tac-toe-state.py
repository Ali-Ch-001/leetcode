"""
794. Valid Tic-Tac-Toe State
Difficulty: Medium
https://leetcode.com/problems/valid-tic-tac-toe-state/

──────────────────────────────────────────────────

Given a Tic-Tac-Toe board as a string array board, return true if and
only if it is possible to reach this board position during the course
of a valid tic-tac-toe game.

The board is a 3 x 3 array that consists of characters ' ', 'X', and
'O'. The ' ' character represents an empty square.

Here are the rules of Tic-Tac-Toe:

	• Players take turns placing characters into empty squares ' '.

• The first player always places 'X' characters, while the second
player always places 'O' characters.

• 'X' and 'O' characters are always placed into empty squares, never
filled ones.

• The game ends when there are three of the same (non-empty)
character filling any row, column, or diagonal.

	• The game also ends if all squares are non-empty.

	• No more moves can be played if the game is over.

 

Example 1:

Input: board = ["O  ","   ","   "]
Output: false
Explanation: The first player always plays "X".

Example 2:

Input: board = ["XOX"," X ","   "]
Output: false
Explanation: Players take turns making moves.

Example 3:

Input: board = ["XOX","O O","XOX"]
Output: true

 

Constraints:

	• board.length == 3

	• board[i].length == 3

	• board[i][j] is either 'X', 'O', or ' '.
"""

class Solution:
    def validTicTacToe(self, board: list[str]) -> bool:
        count_x = sum(row.count("X") for row in board)
        count_o = sum(row.count("O") for row in board)
        if count_x != count_o and count_x != count_o + 1:
            return False

        def wins(player):
            for i in range(3):
                if board[i][0] == board[i][1] == board[i][2] == player:
                    return True
                if board[0][i] == board[1][i] == board[2][i] == player:
                    return True
            if board[0][0] == board[1][1] == board[2][2] == player:
                return True
            if board[0][2] == board[1][1] == board[2][0] == player:
                return True
            return False

        x_wins = wins("X")
        o_wins = wins("O")
        if x_wins and o_wins:
            return False
        if x_wins and count_x != count_o + 1:
            return False
        if o_wins and count_x != count_o:
            return False
        return True
