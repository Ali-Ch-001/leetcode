"""
1473. Paint House III
Difficulty: Hard
https://leetcode.com/problems/paint-house-iii/

──────────────────────────────────────────────────

There is a row of m houses in a small city, each house must be
painted with one of the n colors (labeled from 1 to n), some houses
that have been painted last summer should not be painted again.

A neighborhood is a maximal group of continuous houses that are
painted with the same color.

• For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods
[{1}, {2,2}, {3,3}, {2}, {1,1}].

Given an array houses, an m x n matrix cost and an integer target
where:

• houses[i]: is the color of the house i, and 0 if the house is not
painted yet.

	• cost[i][j]: is the cost of paint the house i with the color j + 1.

Return the minimum cost of painting all the remaining houses in such
a way that there are exactly target neighborhoods. If it is not
possible, return -1.

 

Example 1:

Input: houses = [0,0,0,0,0], cost =
[[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 9
Explanation: Paint houses of this way [1,2,2,1,1]
This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.

Example 2:

Input: houses = [0,2,1,2,0], cost =
[[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 11
Explanation: Some houses are already painted, Paint the houses of
this way [2,2,1,2,2]
This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}]. 
Cost of paint the first and last house (10 + 1) = 11.

Example 3:

Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]],
m = 4, n = 3, target = 3
Output: -1
Explanation: Houses are already painted with a total of 4
neighborhoods [{3},{1},{2},{3}] different of target = 3.

 

Constraints:

	• m == houses.length == cost.length

	• n == cost[i].length

	• 1 <= m <= 100

	• 1 <= n <= 20

	• 1 <= target <= m

	• 0 <= houses[i] <= n

	• 1 <= cost[i][j] <= 10^4
"""

class Solution:
    def minCost(self, houses: list[int], cost: list[list[int]], m: int, n: int, target: int) -> int:
        INF = float('inf')
        dp = [[INF] * (target + 1) for _ in range(n)]
        if houses[0]:
            dp[houses[0] - 1][1] = 0
        else:
            for c in range(n):
                dp[c][1] = cost[0][c]
        for i in range(1, m):
            ndp = [[INF] * (target + 1) for _ in range(n)]
            for k in range(1, target + 1):
                pre = [INF] * (n + 1)
                for c in range(n):
                    pre[c + 1] = pre[c] if pre[c] < dp[c][k - 1] else dp[c][k - 1]
                suf = [INF] * (n + 1)
                for c in range(n - 1, -1, -1):
                    suf[c] = suf[c + 1] if suf[c + 1] < dp[c][k - 1] else dp[c][k - 1]
                for c in range(n):
                    if houses[i] and houses[i] - 1 != c:
                        continue
                    add = 0 if houses[i] else cost[i][c]
                    same = dp[c][k]
                    diff = min(pre[c], suf[c + 1]) if k >= 2 else INF
                    best = same if same < diff else diff
                    if best < INF:
                        ndp[c][k] = best + add
            dp = ndp
        ans = min(dp[c][target] for c in range(n))
        return -1 if ans == INF else ans
        
