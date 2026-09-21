"""
174. Dungeon Game
Difficulty: Hard
https://leetcode.com/problems/dungeon-game/

──────────────────────────────────────────────────

The demons had captured the princess and imprisoned her in the
bottom-right corner of a dungeon. The dungeon consists of m x n rooms
laid out in a 2D grid. Our valiant knight was initially positioned in
the top-left room and must fight his way through dungeon to rescue the
princess.

The knight has an initial health point represented by a positive
integer. If at any point his health point drops to 0 or below, he dies
immediately.

Some of the rooms are guarded by demons (represented by negative
integers), so the knight loses health upon entering these rooms; other
rooms are either empty (represented as 0) or contain magic orbs that
increase the knight's health (represented by positive integers).

To reach the princess as quickly as possible, the knight decides to
move only rightward or downward in each step.

Return the knight's minimum initial health so that he can rescue the
princess.

Note that any room can contain threats or power-ups, even the first
room the knight enters and the bottom-right room where the princess is
imprisoned.

 

Example 1:

Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7
Explanation: The initial health of the knight must be at least 7 if
he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.

Example 2:

Input: dungeon = [[0]]
Output: 1

 

Constraints:

	• m == dungeon.length

	• n == dungeon[i].length

	• 1 <= m, n <= 200

	• -1000 <= dungeon[i][j] <= 1000
"""

class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[0] * cols for _ in range(rows)]
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if r == rows - 1 and c == cols - 1:
                    need = 1 - dungeon[r][c]
                elif r == rows - 1:
                    need = dp[r][c + 1] - dungeon[r][c]
                elif c == cols - 1:
                    need = dp[r + 1][c] - dungeon[r][c]
                else:
                    need = min(dp[r + 1][c], dp[r][c + 1]) - dungeon[r][c]
                dp[r][c] = max(1, need)
        return dp[0][0]
