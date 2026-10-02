"""
1914. Cyclically Rotating a Grid
Difficulty: Medium
https://leetcode.com/problems/cyclically-rotating-a-grid/

──────────────────────────────────────────────────

You are given an m x n integer matrix grid​​​, where m and n are both
even integers, and an integer k.



The matrix is composed of several layers, which is shown in the below
image, where each color is its own layer:






A cyclic rotation of the matrix is done by cyclically rotating each
layer in the matrix. To cyclically rotate a layer once, each element
in the layer will take the place of the adjacent element in the
counter-clockwise direction. An example rotation is shown below:



Return the matrix after applying k cyclic rotations to it.



 



Example 1:




Input: grid = [[40,10],[30,20]], k = 1
Output: [[10,20],[40,30]]
Explanation: The figures above represent the grid at every state.



Example 2:


  


Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
Explanation: The figures above represent the grid at every state.


 


Constraints:




	• m == grid.length

	• n == grid[i].length

	• 2 <= m, n <= 50

	• Both m and n are even integers.

	• 1 <= grid[i][j] <=^ 5000

	• 1 <= k <= 10^9
"""

from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2
        for layer in range(layers):
            top, left = layer, layer
            bottom, right = m - 1 - layer, n - 1 - layer
            elems = []
            for j in range(left, right + 1):
                elems.append(grid[top][j])
            for i in range(top + 1, bottom + 1):
                elems.append(grid[i][right])
            for j in range(right - 1, left - 1, -1):
                elems.append(grid[bottom][j])
            for i in range(bottom - 1, top, -1):
                elems.append(grid[i][left])
            L = len(elems)
            shift = k % L
            idx = 0
            for j in range(left, right + 1):
                grid[top][j] = elems[(idx + shift) % L]
                idx += 1
            for i in range(top + 1, bottom + 1):
                grid[i][right] = elems[(idx + shift) % L]
                idx += 1
            for j in range(right - 1, left - 1, -1):
                grid[bottom][j] = elems[(idx + shift) % L]
                idx += 1
            for i in range(bottom - 1, top, -1):
                grid[i][left] = elems[(idx + shift) % L]
                idx += 1
        return grid
