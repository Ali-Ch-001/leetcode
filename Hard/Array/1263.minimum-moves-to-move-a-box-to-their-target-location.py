"""
1263. Minimum Moves to Move a Box to Their Target Location
Difficulty: Hard
https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/

──────────────────────────────────────────────────

A storekeeper is a game in which the player pushes boxes around in a
warehouse trying to get them to target locations.

The game is represented by an m x n grid of characters grid where
each element is a wall, floor, or box.

Your task is to move the box 'B' to the target position 'T' under the
following rules:

• The character 'S' represents the player. The player can move up,
down, left, right in grid if it is a floor (empty cell).

• The character '.' represents the floor which means a free cell to
walk.

• The character '#' represents the wall which means an obstacle
(impossible to walk there).

	• There is only one box 'B' and one target cell 'T' in the grid.

• The box can be moved to an adjacent free cell by standing next to
the box and then moving in the direction of the box. This is a push.

	• The player cannot walk through the box.

Return the minimum number of pushes to move the box to the target. If
there is no way to reach the target, return -1.

 

Example 1:

Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#",".","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 3
Explanation: We return only the number of times the box is pushed.

Example 2:

Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#","#","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: -1

Example 3:

Input: grid = [["#","#","#","#","#","#"],
               ["#","T",".",".","#","#"],
               ["#",".","#","B",".","#"],
               ["#",".",".",".",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 5
Explanation: push the box down, left, left, up and up.

 

Constraints:

	• m == grid.length

	• n == grid[i].length

	• 1 <= m, n <= 20

	• grid contains only characters '.', '#', 'S', 'T', or 'B'.

	• There is only one character 'S', 'B', and 'T' in the grid.
"""

class Solution:
    def minPushBox(self, grid: list[list[str]]) -> int:
        from collections import deque
        m, n = len(grid), len(grid[0])
        box = player = target = None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'B':
                    box = (i, j)
                elif grid[i][j] == 'S':
                    player = (i, j)
                elif grid[i][j] == 'T':
                    target = (i, j)
        if box == target:
            return 0
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def reachable(start, blocked):
            seen = {start}
            stack = [start]
            while stack:
                x, y = stack.pop()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen
                            and (nx, ny) != blocked and grid[nx][ny] != '#'):
                        seen.add((nx, ny))
                        stack.append((nx, ny))
            return seen

        comp = reachable(player, box)
        q = deque()
        visited = set()
        for dx, dy in dirs:
            nb = (box[0] + dx, box[1] + dy)
            fr = (box[0] - dx, box[1] - dy)
            if fr in comp and 0 <= nb[0] < m and 0 <= nb[1] < n and grid[nb[0]][nb[1]] != '#':
                state = (nb, box)
                if state not in visited:
                    visited.add(state)
                    if nb == target:
                        return 1
                    q.append((nb, box, 1))
        while q:
            b, p, pushes = q.popleft()
            comp = reachable(p, b)
            for dx, dy in dirs:
                nb = (b[0] + dx, b[1] + dy)
                fr = (b[0] - dx, b[1] - dy)
                if fr in comp and 0 <= nb[0] < m and 0 <= nb[1] < n and grid[nb[0]][nb[1]] != '#':
                    state = (nb, b)
                    if state not in visited:
                        visited.add(state)
                        if nb == target:
                            return pushes + 1
                        q.append((nb, b, pushes + 1))
        return -1
