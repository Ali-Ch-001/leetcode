"""
212. Word Search II
Difficulty: Hard
https://leetcode.com/problems/word-search-ii/

──────────────────────────────────────────────────

Given an m x n board of characters and a list of strings words,
return all words on the board.

Each word must be constructed from letters of sequentially adjacent
cells, where adjacent cells are horizontally or vertically
neighboring. The same letter cell may not be used more than once in a
word.

 

Example 1:

Input: board =
[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

 

Constraints:

	• m == board.length

	• n == board[i].length

	• 1 <= m, n <= 12

	• board[i][j] is a lowercase English letter.

	• 1 <= words.length <= 3 * 10^4

	• 1 <= words[i].length <= 10

	• words[i] consists of lowercase English letters.

	• All the strings of words are unique.
"""

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node["#"] = word
        rows, cols = len(board), len(board[0])
        found = []

        def dfs(r: int, c: int, node: dict) -> None:
            ch = board[r][c]
            nxt = node.get(ch)
            if nxt is None:
                return
            if "#" in nxt:
                found.append(nxt["#"])
                del nxt["#"]
            board[r][c] = "@"
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "@":
                    dfs(nr, nc, nxt)
            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)
        return found
