"""
407. Trapping Rain Water II
Difficulty: Hard
https://leetcode.com/problems/trapping-rain-water-ii/

──────────────────────────────────────────────────

Given an m x n integer matrix heightMap representing the height of
each unit cell in a 2D elevation map, return the volume of water it
can trap after raining.

 

Example 1:

Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.

Example 2:

Input: heightMap =
[[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10

 

Constraints:

	• m == heightMap.length

	• n == heightMap[i].length

	• 1 <= m, n <= 200

	• 0 <= heightMap[i][j] <= 2 * 10^4
"""

import heapq


class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        rows, cols = len(heightMap), len(heightMap[0])
        visited = [[False] * cols for _ in range(rows)]
        heap = []
        for r in range(rows):
            for c in range(cols):
                if r in (0, rows - 1) or c in (0, cols - 1):
                    heapq.heappush(heap, (heightMap[r][c], r, c))
                    visited[r][c] = True
        water = 0
        level = 0
        while heap:
            height, r, c = heapq.heappop(heap)
            level = max(level, height)
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    visited[nr][nc] = True
                    water += max(0, level - heightMap[nr][nc])
                    heapq.heappush(heap, (heightMap[nr][nc], nr, nc))
        return water
