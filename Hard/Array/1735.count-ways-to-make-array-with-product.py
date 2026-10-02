"""
1735. Count Ways to Make Array With Product
Difficulty: Hard
https://leetcode.com/problems/count-ways-to-make-array-with-product/

──────────────────────────────────────────────────

You are given a 2D integer array, queries. For each queries[i], where
queries[i] = [ni, ki], find the number of different ways you can place
positive integers into an array of size ni such that the product of
the integers is ki. As the number of ways may be too large, the answer
to the i^th query is the number of ways modulo 10^9 + 7.

Return an integer array answer where answer.length == queries.length,
and answer[i] is the answer to the i^th query.

 

Example 1:

Input: queries = [[2,6],[5,1],[73,660]]
Output: [4,1,50734910]
Explanation: Each query is independent.
[2,6]: There are 4 ways to fill an array of size 2 that multiply to
6: [1,6], [2,3], [3,2], [6,1].
[5,1]: There is 1 way to fill an array of size 5 that multiply to 1:
[1,1,1,1,1].
[73,660]: There are 1050734917 ways to fill an array of size 73 that
multiply to 660. 1050734917 modulo 10^9 + 7 = 50734910.

Example 2:

Input: queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]
Output: [1,2,3,10,5]

 

Constraints:

	• 1 <= queries.length <= 10^4 

	• 1 <= ni, ki <= 10^4
"""

class Solution:
    def waysToFillArray(self, queries: list[list[int]]) -> list[int]:
        MOD = 10 ** 9 + 7
        max_n = max(q[0] for q in queries)
        limit = max_n + 20
        fact = [1] * limit
        for i in range(1, limit):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * limit
        inv_fact[limit - 1] = pow(fact[limit - 1], MOD - 2, MOD)
        for i in range(limit - 1, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        ans = []
        for ni, ki in queries:
            res = 1
            x = ki
            d = 2
            while d * d <= x:
                if x % d == 0:
                    e = 0
                    while x % d == 0:
                        x //= d
                        e += 1
                    res = res * comb(e + ni - 1, e) % MOD
                d += 1
            if x > 1:
                res = res * comb(ni, 1) % MOD
            ans.append(res)
        return ans
