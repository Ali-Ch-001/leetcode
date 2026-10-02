"""
2018. Check if Word Can Be Placed In Crossword
Difficulty: Medium
https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/

──────────────────────────────────────────────────

You are given an m x n matrix board, representing the current state
of a crossword puzzle. The crossword contains lowercase English
letters (from solved words), ' ' to represent any empty cells, and '#'
to represent any blocked cells.

A word can be placed horizontally (left to right or right to left) or
vertically (top to bottom or bottom to top) in the board if:

	• It does not occupy a cell containing the character '#'.

• The cell each letter is placed in must either be ' ' (empty) or
match the letter already on the board.

• There must not be any empty cells ' ' or other lowercase letters
directly left or right of the word if the word was placed
horizontally.

• There must not be any empty cells ' ' or other lowercase letters
directly above or below the word if the word was placed vertically.

Given a string word, return true if word can be placed in board, or
false otherwise.

 

Example 1:

Input: board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]],
word = "abc"
Output: true
Explanation: The word "abc" can be placed as shown above (top to
bottom).

Example 2:

Input: board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]],
word = "ac"
Output: false
Explanation: It is impossible to place the word because there will
always be a space/letter above or below it.

Example 3:

Input: board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]],
word = "ca"
Output: true
Explanation: The word "ca" can be placed as shown above (right to
left).

 

Constraints:

	• m == board.length

	• n == board[i].length

	• 1 <= m * n <= 2 * 10^5

	• board[i][j] will be ' ', '#', or a lowercase English letter.

	• 1 <= word.length <= max(m, n)

	• word will contain only lowercase English letters.
"""

class Solution:
    def placeWordInCrossword(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        L = len(word)
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for r in range(m):
            for c in range(n):
                for dr, dc in dirs:
                    er, ec = r + dr * (L - 1), c + dc * (L - 1)
                    if not (0 <= er < m and 0 <= ec < n):
                        continue
                    br, bc = r - dr, c - dc
                    if 0 <= br < m and 0 <= bc < n and board[br][bc] != '#':
                        continue
                    ar, ac = er + dr, ec + dc
                    if 0 <= ar < m and 0 <= ac < n and board[ar][ac] != '#':
                        continue
                    ok = True
                    for k in range(L):
                        cell = board[r + dr * k][c + dc * k]
                        if cell != ' ' and cell != word[k]:
                            ok = False
                            break
                    if ok:
                        return True
        return False
