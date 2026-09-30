"""
1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
Difficulty: Medium
https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

──────────────────────────────────────────────────

Given a m x n matrix mat and an integer threshold, return the maximum
side-length of a square with a sum less than or equal to threshold or
return 0 if there is no such square.

 

Example 1:

Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]],
threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than or
equal to 4 is 2 as shown.

Example 2:

Input: mat =
[[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]],
threshold = 1
Output: 0

 

Constraints:

	• m == mat.length

	• n == mat[i].length

	• 1 <= m, n <= 300

	• 0 <= mat[i][j] <= 10^4

	• 0 <= threshold <= 10^5
"""

class Solution:
    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += mat[i][j]
                pre[i + 1][j + 1] = pre[i][j + 1] + row_sum

        def exists(side: int) -> bool:
            for i in range(m - side + 1):
                for j in range(n - side + 1):
                    s = pre[i + side][j + side] - pre[i][j + side] - pre[i + side][j] + pre[i][j]
                    if s <= threshold:
                        return True
            return False

        lo, hi, ans = 1, min(m, n), 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if exists(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
