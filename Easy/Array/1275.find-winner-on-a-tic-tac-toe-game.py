"""
1275. Find Winner on a Tic Tac Toe Game
Difficulty: Easy
https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

──────────────────────────────────────────────────

Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The
rules of Tic-Tac-Toe are:

	• Players take turns placing characters into empty squares ' '.

• The first player A always places 'X' characters, while the second
player B always places 'O' characters.

• 'X' and 'O' characters are always placed into empty squares, never
on filled ones.

• The game ends when there are three of the same (non-empty)
character filling any row, column, or diagonal.

	• The game also ends if all squares are non-empty.

	• No more moves can be played if the game is over.

Given a 2D integer array moves where moves[i] = [rowi, coli]
indicates that the i^th move will be played on grid[rowi][coli].
return the winner of the game if it exists (A or B). In case the game
ends in a draw return "Draw". If there are still movements to play
return "Pending".

You can assume that moves is valid (i.e., it follows the rules of
Tic-Tac-Toe), the grid is initially empty, and A will play first.

 

Example 1:

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.

Example 2:

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: B wins.

Example 3:

Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.

 

Constraints:

	• 1 <= moves.length <= 9

	• moves[i].length == 2

	• 0 <= rowi, coli <= 2

	• There are no repeated elements on moves.

	• moves follow the rules of tic tac toe.
"""

class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        board = [[' '] * 3 for _ in range(3)]

        def wins(ch: str) -> bool:
            for i in range(3):
                if all(board[i][j] == ch for j in range(3)):
                    return True
                if all(board[j][i] == ch for j in range(3)):
                    return True
            if all(board[i][i] == ch for i in range(3)):
                return True
            if all(board[i][2 - i] == ch for i in range(3)):
                return True
            return False

        for idx, (r, c) in enumerate(moves):
            board[r][c] = 'X' if idx % 2 == 0 else 'O'

        if wins('X'):
            return "A"
        if wins('O'):
            return "B"
        return "Draw" if len(moves) == 9 else "Pending"
