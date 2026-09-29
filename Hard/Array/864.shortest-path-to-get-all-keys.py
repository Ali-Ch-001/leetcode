"""
864. Shortest Path to Get All Keys
Difficulty: Hard
https://leetcode.com/problems/shortest-path-to-get-all-keys/

──────────────────────────────────────────────────

You are given an m x n grid grid where:

	• '.' is an empty cell.

	• '#' is a wall.

	• '@' is the starting point.

	• Lowercase letters represent keys.

	• Uppercase letters represent locks.

You start at the starting point and one move consists of walking one
space in one of the four cardinal directions. You cannot walk outside
the grid, or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a
lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one
uppercase letter of the first k letters of the English alphabet in the
grid. This means that there is exactly one key for each lock, and one
lock for each key; and also that the letters used to represent the
keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys. If it is
impossible, return -1.

 

Example 1:

Input: grid = ["@.a..","###.#","b.A.B"]
Output: 8
Explanation: Note that the goal is to obtain all the keys not to open
all the locks.

Example 2:

Input: grid = ["@..aA","..B#.","....b"]
Output: 6

Example 3:

Input: grid = ["@Aa"]
Output: -1

 

Constraints:

	• m == grid.length

	• n == grid[i].length

	• 1 <= m, n <= 30

	• grid[i][j] is either an English letter, '.', '#', or '@'. 

	• There is exactly one '@' in the grid.

	• The number of keys in the grid is in the range [1, 6].

	• Each key in the grid is unique.

	• Each key in the grid has a matching lock.
"""

from collections import deque


class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        rows, cols = len(grid), len(grid[0])
        start = None
        keys_needed = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "@":
                    start = (r, c)
                elif "a" <= grid[r][c] <= "f":
                    keys_needed |= 1 << (ord(grid[r][c]) - ord("a"))
        full = keys_needed
        queue = deque([(start[0], start[1], 0, 0)])
        visited = {(start[0], start[1], 0)}
        while queue:
            r, c, keys, distance = queue.popleft()
            if keys == full:
                return distance
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue
                cell = grid[nr][nc]
                if cell == "#":
                    continue
                new_keys = keys
                if "a" <= cell <= "f":
                    new_keys |= 1 << (ord(cell) - ord("a"))
                elif "A" <= cell <= "F":
                    if not (keys & (1 << (ord(cell) - ord("A")))):
                        continue
                state = (nr, nc, new_keys)
                if state not in visited:
                    visited.add(state)
                    queue.append((nr, nc, new_keys, distance + 1))
        return -1
