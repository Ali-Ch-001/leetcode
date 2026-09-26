"""
546. Remove Boxes
Difficulty: Hard
https://leetcode.com/problems/remove-boxes/

──────────────────────────────────────────────────

You are given several boxes with different colors represented by
different positive numbers.

You may experience several rounds to remove boxes until there is no
box left. Each time you can choose some continuous boxes with the same
color (i.e., composed of k boxes, k >= 1), remove them and get k * k
points.

Return the maximum points you can get.

 

Example 1:

Input: boxes = [1,3,2,2,2,3,4,3,1]
Output: 23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
----> [1, 3, 3, 3, 1] (1*1=1 points) 
----> [1, 1] (3*3=9 points) 
----> [] (2*2=4 points)

Example 2:

Input: boxes = [1,1,1]
Output: 9

Example 3:

Input: boxes = [1]
Output: 1

 

Constraints:

	• 1 <= boxes.length <= 100

	• 1 <= boxes[i] <= 100
"""

import sys
from bisect import bisect_right
from functools import lru_cache


class Solution:
    def removeBoxes(self, boxes: list[int]) -> int:
        sys.setrecursionlimit(10000)
        colors = []
        counts = []
        for value in boxes:
            if colors and colors[-1] == value:
                counts[-1] += 1
            else:
                colors.append(value)
                counts.append(1)
        n = len(colors)
        positions = {}
        for index, color in enumerate(colors):
            positions.setdefault(color, []).append(index)

        @lru_cache(maxsize=None)
        def dp(i: int, j: int, k: int) -> int:
            if i > j:
                return 0
            best = (counts[i] + k) ** 2 + dp(i + 1, j, 0)
            lst = positions[colors[i]]
            start = bisect_right(lst, i)
            for idx in range(start, len(lst)):
                m = lst[idx]
                if m > j:
                    break
                candidate = dp(i + 1, m - 1, 0) + dp(m, j, counts[i] + k)
                if candidate > best:
                    best = candidate
            return best

        result = dp(0, n - 1, 0)
        dp.cache_clear()
        return result
