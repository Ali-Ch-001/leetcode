"""
959. Regions Cut By Slashes
Difficulty: Medium
https://leetcode.com/problems/regions-cut-by-slashes/

──────────────────────────────────────────────────

An n x n grid is composed of 1 x 1 squares where each 1 x 1 square
consists of a '/', '\', or blank space ' '. These characters divide
the square into contiguous regions.

Given the grid grid represented as a string array, return the number
of regions.

Note that backslash characters are escaped, so a '\' is represented
as '\\'.

 

Example 1:

Input: grid = [" /","/ "]
Output: 2

Example 2:

Input: grid = [" /","  "]
Output: 1

Example 3:

Input: grid = ["/\\","\\/"]
Output: 5
Explanation: Recall that because \ characters are escaped, "\\/"
refers to \/, and "/\\" refers to /\.

 

Constraints:

	• n == grid.length == grid[i].length

	• 1 <= n <= 30

	• grid[i][j] is either '/', '\', or ' '.
"""

class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        n = len(grid)
        parent = list(range(4 * n * n))
        rank = [0] * (4 * n * n)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            root_a, root_b = find(a), find(b)
            if root_a == root_b:
                return
            if rank[root_a] < rank[root_b]:
                root_a, root_b = root_b, root_a
            parent[root_b] = root_a
            if rank[root_a] == rank[root_b]:
                rank[root_a] += 1

        for r in range(n):
            for c in range(n):
                base = 4 * (r * n + c)
                ch = grid[r][c]
                if ch == "/":
                    union(base + 0, base + 3)
                    union(base + 1, base + 2)
                elif ch == "\\":
                    union(base + 0, base + 1)
                    union(base + 2, base + 3)
                else:
                    union(base + 0, base + 1)
                    union(base + 1, base + 2)
                    union(base + 2, base + 3)
                if r > 0:
                    union(base + 0, 4 * ((r - 1) * n + c) + 2)
                if c > 0:
                    union(base + 3, 4 * (r * n + c - 1) + 1)
        return len({find(i) for i in range(4 * n * n)})
