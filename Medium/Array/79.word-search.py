"""
79. Word Search
Difficulty: Medium
https://leetcode.com/problems/word-search/

──────────────────────────────────────────────────

Given an m x n grid of characters board and a string word, return
true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent
cells, where adjacent cells are horizontally or vertically
neighboring. The same letter cell may not be used more than once.

 

Example 1:

Input: board =
[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
"ABCCED"
Output: true

Example 2:

Input: board =
[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board =
[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

 

Constraints:

	• m == board.length

	• n = board[i].length

	• 1 <= m, n <= 6

	• 1 <= word.length <= 15

• board and word consists of only lowercase and uppercase English
letters.

 

Follow up: Could you use search pruning to make your solution faster
with a larger board?
"""

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int, index: int) -> bool:
            if index == len(word):
                return True
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[index]:
                return False
            saved = board[r][c]
            board[r][c] = "#"
            found = (
                dfs(r + 1, c, index + 1)
                or dfs(r - 1, c, index + 1)
                or dfs(r, c + 1, index + 1)
                or dfs(r, c - 1, index + 1)
            )
            board[r][c] = saved
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
