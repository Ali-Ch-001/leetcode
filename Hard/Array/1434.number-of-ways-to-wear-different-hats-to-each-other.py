"""
1434. Number of Ways to Wear Different Hats to Each Other
Difficulty: Hard
https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/

──────────────────────────────────────────────────

There are n people and 40 types of hats labeled from 1 to 40.

Given a 2D integer array hats, where hats[i] is a list of all hats
preferred by the i^th person.

Return the number of ways that n people can wear different hats from
each other.

Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: hats = [[3,4],[4,5],[5]]
Output: 1
Explanation: There is only one way to choose hats given the
conditions.
First person chooses hat 3, Second person chooses hat 4 and last one
hat 5.

Example 2:

Input: hats = [[3,5,1],[3,5]]
Output: 4
Explanation: There are 4 ways to choose hats:
(3,5), (5,3), (1,3) and (1,5)

Example 3:

Input: hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
Output: 24
Explanation: Each person can choose hats labeled from 1 to 4.
Number of Permutations of (1,2,3,4) = 24.

 

Constraints:

	• n == hats.length

	• 1 <= n <= 10

	• 1 <= hats[i].length <= 40

	• 1 <= hats[i][j] <= 40

	• hats[i] contains a list of unique integers.
"""

class Solution:
    def numberWays(self, hats: list[list[int]]) -> int:
        MOD = 10**9 + 7
        n = len(hats)
        full = (1 << n) - 1
        hat_to_people = [[] for _ in range(41)]
        for i, hs in enumerate(hats):
            for h in hs:
                hat_to_people[h].append(i)
        dp = [0] * (1 << n)
        dp[0] = 1
        for h in range(1, 41):
            people = hat_to_people[h]
            if not people:
                continue
            ndp = dp[:]
            for mask in range(1 << n):
                if dp[mask] == 0:
                    continue
                for i in people:
                    if not (mask >> i) & 1:
                        ndp[mask | (1 << i)] = (ndp[mask | (1 << i)] + dp[mask]) % MOD
            dp = ndp
        return dp[full]
