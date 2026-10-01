"""
1595. Minimum Cost to Connect Two Groups of Points
Difficulty: Hard
https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/

──────────────────────────────────────────────────

You are given two groups of points where the first group has size1
points, the second group has size2 points, and size1 >= size2.

The cost of the connection between any two points are given in an
size1 x size2 matrix where cost[i][j] is the cost of connecting point
i of the first group and point j of the second group. The groups are
connected if each point in both groups is connected to one or more
points in the opposite group. In other words, each point in the first
group must be connected to at least one point in the second group, and
each point in the second group must be connected to at least one point
in the first group.

Return the minimum cost it takes to connect the two groups.

 

Example 1:

Input: cost = [[15, 96], [36, 2]]
Output: 17
Explanation: The optimal way of connecting the groups is:
1--A
2--B
This results in a total cost of 17.

Example 2:

Input: cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
Output: 4
Explanation: The optimal way of connecting the groups is:
1--A
2--B
2--C
3--A
This results in a total cost of 4.
Note that there are multiple points connected to point 2 in the first
group and point A in the second group. This does not matter as there
is no limit to the number of points that can be connected. We only
care about the minimum total cost.

Example 3:

Input: cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
Output: 10

 

Constraints:

	• size1 == cost.length

	• size2 == cost[i].length

	• 1 <= size1, size2 <= 12

	• size1 >= size2

	• 0 <= cost[i][j] <= 100
"""

class Solution:
    def connectTwoGroups(self, cost: list[list[int]]) -> int:
        n, m = len(cost), len(cost[0])
        min_col = [min(cost[i][j] for i in range(n)) for j in range(m)]
        INF = float('inf')
        dp = [INF] * (1 << m)
        dp[0] = 0
        for i in range(n):
            ndp = [INF] * (1 << m)
            for mask in range(1 << m):
                if dp[mask] == INF:
                    continue
                for j in range(m):
                    nmask = mask | (1 << j)
                    val = dp[mask] + cost[i][j]
                    if val < ndp[nmask]:
                        ndp[nmask] = val
            dp = ndp
        ans = INF
        for mask in range(1 << m):
            if dp[mask] == INF:
                continue
            remaining = 0
            for j in range(m):
                if not (mask >> j) & 1:
                    remaining += min_col[j]
            total = dp[mask] + remaining
            if total < ans:
                ans = total
        return ans
