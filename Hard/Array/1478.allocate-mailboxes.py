"""
1478. Allocate Mailboxes
Difficulty: Hard
https://leetcode.com/problems/allocate-mailboxes/

──────────────────────────────────────────────────

Given the array houses where houses[i] is the location of the i^th
house along a street and an integer k, allocate k mailboxes in the
street.

Return the minimum total distance between each house and its nearest
mailbox.

The test cases are generated so that the answer fits in a 32-bit
integer.

 

Example 1:

Input: houses = [1,4,8,10,20], k = 3
Output: 5
Explanation: Allocate mailboxes in position 3, 9 and 20.
Minimum total distance from each houses to nearest mailboxes is |3-1|
+ |4-3| + |9-8| + |10-9| + |20-20| = 5

Example 2:

Input: houses = [2,3,5,12,18], k = 2
Output: 9
Explanation: Allocate mailboxes in position 3 and 14.
Minimum total distance from each houses to nearest mailboxes is |2-3|
+ |3-3| + |5-3| + |12-14| + |18-14| = 9.

 

Constraints:

	• 1 <= k <= houses.length <= 100

	• 1 <= houses[i] <= 10^4

	• All the integers of houses are unique.
"""

class Solution:
    def minDistance(self, houses: list[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        pre = [0] * (n + 1)
        for i, h in enumerate(houses):
            pre[i + 1] = pre[i] + h

        def seg(i: int, j: int) -> int:
            mid = (i + j) // 2
            left = houses[mid] * (mid - i + 1) - (pre[mid + 1] - pre[i])
            right = (pre[j + 1] - pre[mid + 1]) - houses[mid] * (j - mid)
            return left + right

        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0
        for g in range(1, k + 1):
            ndp = [INF] * (n + 1)
            for i in range(g, n + 1):
                best = INF
                for p in range(g - 1, i):
                    if dp[p] < INF:
                        v = dp[p] + seg(p, i - 1)
                        if v < best:
                            best = v
                ndp[i] = best
            dp = ndp
        return dp[n]
        
