"""
913. Cat and Mouse
Difficulty: Hard
https://leetcode.com/problems/cat-and-mouse/

──────────────────────────────────────────────────

A game on an undirected graph is played by two players, Mouse and
Cat, who alternate turns.

The graph is given as follows: graph[a] is a list of all nodes b such
that ab is an edge of the graph.

The mouse starts at node 1 and goes first, the cat starts at node 2
and goes second, and there is a hole at node 0.

During each player's turn, they must travel along one edge of the
graph that meets where they are.  For example, if the Mouse is at node
1, it must travel to any node in graph[1].

Additionally, it is not allowed for the Cat to travel to the Hole
(node 0).

Then, the game can end in three ways:

	• If ever the Cat occupies the same node as the Mouse, the Cat wins.

	• If ever the Mouse reaches the Hole, the Mouse wins.

• If ever a position is repeated (i.e., the players are in the same
position as a previous turn, and it is the same player's turn to
move), the game is a draw.

Given a graph, and assuming both players play optimally, return

	• 1 if the mouse wins the game,

	• 2 if the cat wins the game, or

	• 0 if the game is a draw.

 

Example 1:

Input: graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
Output: 0

Example 2:

Input: graph = [[1,3],[0],[3],[0,2]]
Output: 1

 

Constraints:

	• 3 <= graph.length <= 50

	• 1 <= graph[i].length < graph.length

	• 0 <= graph[i][j] < graph.length

	• graph[i][j] != i

	• graph[i] is unique.

	• The mouse and the cat can always move.
"""

from collections import deque


class Solution:
    def catMouseGame(self, graph: list[list[int]]) -> int:
        n = len(graph)
        DRAW, MOUSE, CAT = 0, 1, 2
        color = [[[DRAW] * 3 for _ in range(n)] for _ in range(n)]
        degree = [[[0] * 3 for _ in range(n)] for _ in range(n)]
        for m in range(n):
            for c in range(n):
                degree[m][c][1] = len(graph[m])
                degree[m][c][2] = len(graph[c]) - (1 if 0 in graph[c] else 0)
        queue = deque()
        for c in range(n):
            color[0][c][1] = MOUSE
            color[0][c][2] = MOUSE
            queue.append((0, c, 1))
            queue.append((0, c, 2))
        for x in range(1, n):
            color[x][x][1] = CAT
            color[x][x][2] = CAT
            queue.append((x, x, 1))
            queue.append((x, x, 2))
        while queue:
            mouse, cat, turn = queue.popleft()
            current = color[mouse][cat][turn]
            if turn == 1:
                for prev in graph[cat]:
                    if prev == 0:
                        continue
                    if color[mouse][prev][2] != DRAW:
                        continue
                    if current == CAT:
                        color[mouse][prev][2] = CAT
                        queue.append((mouse, prev, 2))
                    else:
                        degree[mouse][prev][2] -= 1
                        if degree[mouse][prev][2] == 0:
                            color[mouse][prev][2] = MOUSE
                            queue.append((mouse, prev, 2))
            else:
                for prev in graph[mouse]:
                    if color[prev][cat][1] != DRAW:
                        continue
                    if current == MOUSE:
                        color[prev][cat][1] = MOUSE
                        queue.append((prev, cat, 1))
                    else:
                        degree[prev][cat][1] -= 1
                        if degree[prev][cat][1] == 0:
                            color[prev][cat][1] = CAT
                            queue.append((prev, cat, 1))
        return color[1][2][1]
