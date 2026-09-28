"""
749. Contain Virus
Difficulty: Hard
https://leetcode.com/problems/contain-virus/

──────────────────────────────────────────────────

A virus is spreading rapidly, and your task is to quarantine the
infected area by installing walls.

The world is modeled as an m x n binary grid isInfected, where
isInfected[i][j] == 0 represents uninfected cells, and
isInfected[i][j] == 1 represents cells contaminated with the virus. A
wall (and only one wall) can be installed between any two
4-directionally adjacent cells, on the shared boundary.

Every night, the virus spreads to all neighboring cells in all four
directions unless blocked by a wall. Resources are limited. Each day,
you can install walls around only one region (i.e., the affected area
(continuous block of infected cells) that threatens the most
uninfected cells the following night). There will never be a tie.

Return the number of walls used to quarantine all the infected
regions. If the world will become fully infected, return the number of
walls used.

 

Example 1:

Input: isInfected =
[[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
Output: 10
Explanation: There are 2 contaminated regions.
On the first day, add 5 walls to quarantine the viral region on the
left. The board after the virus spreads is:

On the second day, add 5 walls to quarantine the viral region on the
right. The virus is fully contained.

Example 2:

Input: isInfected = [[1,1,1],[1,0,1],[1,1,1]]
Output: 4
Explanation: Even though there is only one cell saved, there are 4
walls built.
Notice that walls are only built on the shared boundary of two
different cells.

Example 3:

Input: isInfected =
[[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
Output: 13
Explanation: The region on the left only builds two new walls.

 

Constraints:

	• m == isInfected.length

	• n == isInfected[i].length

	• 1 <= m, n <= 50

	• isInfected[i][j] is either 0 or 1.

• There is always a contiguous viral region throughout the described
process that will infect strictly more uncontaminated squares in the
next round.
"""

class Solution:
    def containVirus(self, isInfected: list[list[int]]) -> int:
        rows, cols = len(isInfected), len(isInfected[0])
        total_walls = 0
        while True:
            visited = [[False] * cols for _ in range(rows)]
            regions = []
            for r in range(rows):
                for c in range(cols):
                    if isInfected[r][c] == 1 and not visited[r][c]:
                        cells = []
                        frontier = set()
                        walls = 0
                        stack = [(r, c)]
                        visited[r][c] = True
                        while stack:
                            x, y = stack.pop()
                            cells.append((x, y))
                            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                                if 0 <= nx < rows and 0 <= ny < cols:
                                    if isInfected[nx][ny] == 1 and not visited[nx][ny]:
                                        visited[nx][ny] = True
                                        stack.append((nx, ny))
                                    elif isInfected[nx][ny] == 0:
                                        frontier.add((nx, ny))
                                        walls += 1
                        regions.append({"cells": cells, "frontier": frontier, "walls": walls})
            if not regions:
                break
            if all(len(region["frontier"]) == 0 for region in regions):
                break
            target = max(regions, key=lambda region: len(region["frontier"]))
            total_walls += target["walls"]
            for x, y in target["cells"]:
                isInfected[x][y] = -1
            for region in regions:
                if region is target:
                    continue
                for x, y in region["frontier"]:
                    isInfected[x][y] = 1
        return total_walls
