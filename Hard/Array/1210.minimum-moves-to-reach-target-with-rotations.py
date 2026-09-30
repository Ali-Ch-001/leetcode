"""
1210. Minimum Moves to Reach Target with Rotations
Difficulty: Hard
https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/

──────────────────────────────────────────────────

In an n*n grid, there is a snake that spans 2 cells and starts moving
from the top left corner at (0, 0) and (0, 1). The grid has empty
cells represented by zeros and blocked cells represented by ones. The
snake wants to reach the lower right corner at (n-1, n-2) and (n-1,
n-1).

In one move the snake can:

• Move one cell to the right if there are no blocked cells there.
This move keeps the horizontal/vertical position of the snake as it
is.

• Move down one cell if there are no blocked cells there. This move
keeps the horizontal/vertical position of the snake as it is.

• Rotate clockwise if it's in a horizontal position and the two
cells under it are both empty. In that case the snake moves from (r,
c) and (r, c+1) to (r, c) and (r+1, c).

	

• Rotate counterclockwise if it's in a vertical position and the two
cells to its right are both empty. In that case the snake moves from
(r, c) and (r+1, c) to (r, c) and (r, c+1).

	

Return the minimum number of moves to reach the target.

If there is no way to reach the target, return -1.

 

Example 1:

Input: grid = [[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]]
Output: 11
Explanation:
One possible solution is [right, right, rotate clockwise, right,
down, down, down, down, rotate counterclockwise, right, down].

Example 2:

Input: grid = [[0,0,1,1,1,1],
               [0,0,0,0,1,1],
               [1,1,0,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,0]]
Output: 9

 

Constraints:

	• 2 <= n <= 100

	• 0 <= grid[i][j] <= 1

	• It is guaranteed that the snake starts at empty cells.
"""

from collections import deque

class Solution:
    def minimumMoves(self, grid: list[list[int]]) -> int:
        n = len(grid)
        start = (0, 0, 0)
        target = (n - 1, n - 2, 0)
        if n == 1:
            return 0
        dist = {start: 0}
        q = deque([start])
        while q:
            r, c, o = q.popleft()
            d = dist[(r, c, o)]
            if (r, c, o) == target:
                return d
            nxt = []
            if o == 0:
                if c + 2 < n and grid[r][c + 2] == 0:
                    nxt.append((r, c + 1, 0))
                if r + 1 < n and grid[r + 1][c] == 0 and grid[r + 1][c + 1] == 0:
                    nxt.append((r + 1, c, 0))
                    nxt.append((r, c, 1))
            else:
                if r + 2 < n and grid[r + 2][c] == 0:
                    nxt.append((r + 1, c, 1))
                if c + 1 < n and grid[r][c + 1] == 0 and grid[r + 1][c + 1] == 0:
                    nxt.append((r, c + 1, 1))
                    nxt.append((r, c, 0))
            for s in nxt:
                if s not in dist:
                    dist[s] = d + 1
                    q.append(s)
        return -1
        
