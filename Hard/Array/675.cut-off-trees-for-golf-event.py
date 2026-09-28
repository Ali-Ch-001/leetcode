"""
675. Cut Off Trees for Golf Event
Difficulty: Hard
https://leetcode.com/problems/cut-off-trees-for-golf-event/

──────────────────────────────────────────────────

You are asked to cut off all the trees in a forest for a golf event.
The forest is represented as an m x n matrix. In this matrix:

	• 0 means the cell cannot be walked through.

	• 1 represents an empty cell that can be walked through.

• A number greater than 1 represents a tree in a cell that can be
walked through, and this number is the tree's height.

In one step, you can walk in any of the four directions: north, east,
south, and west. If you are standing in a cell with a tree, you can
choose whether to cut it off.

You must cut off the trees in order from shortest to tallest. When
you cut off a tree, the value at its cell becomes 1 (an empty cell).

Starting from the point (0, 0), return the minimum steps you need to
walk to cut off all the trees. If you cannot cut off all the trees,
return -1.

Note: The input is generated such that no two trees have the same
height, and there is at least one tree needs to be cut off.

 

Example 1:

Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
Output: 6
Explanation: Following the path above allows you to cut off the trees
from shortest to tallest in 6 steps.

Example 2:

Input: forest = [[1,2,3],[0,0,0],[7,6,5]]
Output: -1
Explanation: The trees in the bottom row cannot be accessed as the
middle row is blocked.

Example 3:

Input: forest = [[2,3,4],[0,0,5],[8,7,6]]
Output: 6
Explanation: You can follow the same path as Example 1 to cut off all
the trees.
Note that you can cut off the first tree at (0, 0) before making any
steps.

 

Constraints:

	• m == forest.length

	• n == forest[i].length

	• 1 <= m, n <= 50

	• 0 <= forest[i][j] <= 10^9

	• Heights of all trees are distinct.
"""

from collections import deque


class Solution:
    def cutOffTree(self, forest: list[list[int]]) -> int:
        if not forest or not forest[0]:
            return -1
        rows, cols = len(forest), len(forest[0])
        trees = sorted(
            (forest[r][c], r, c) for r in range(rows) for c in range(cols) if forest[r][c] > 1
        )

        def bfs(start_r, start_c, target_r, target_c):
            if start_r == target_r and start_c == target_c:
                return 0
            visited = [[False] * cols for _ in range(rows)]
            visited[start_r][start_c] = True
            queue = deque([(start_r, start_c, 0)])
            while queue:
                r, c, steps = queue.popleft()
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and forest[nr][nc] != 0:
                        if nr == target_r and nc == target_c:
                            return steps + 1
                        visited[nr][nc] = True
                        queue.append((nr, nc, steps + 1))
            return -1

        total = 0
        r = c = 0
        for _, tr, tc in trees:
            distance = bfs(r, c, tr, tc)
            if distance == -1:
                return -1
            total += distance
            r, c = tr, tc
        return total
