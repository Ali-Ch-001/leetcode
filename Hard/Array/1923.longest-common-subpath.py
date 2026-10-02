"""
1923. Longest Common Subpath
Difficulty: Hard
https://leetcode.com/problems/longest-common-subpath/

──────────────────────────────────────────────────

There is a country of n cities numbered from 0 to n - 1. In this
country, there is a road connecting every pair of cities.

There are m friends numbered from 0 to m - 1 who are traveling
through the country. Each one of them will take a path consisting of
some cities. Each path is represented by an integer array that
contains the visited cities in order. The path may contain a city more
than once, but the same city will not be listed consecutively.

Given an integer n and a 2D integer array paths where paths[i] is an
integer array representing the path of the i^th friend, return the
length of the longest common subpath that is shared by every friend's
path, or 0 if there is no common subpath at all.

A subpath of a path is a contiguous sequence of cities within that
path.

 

Example 1:

Input: n = 5, paths = [[0,1,2,3,4],
                       [2,3,4],
                       [4,0,1,2,3]]
Output: 2
Explanation: The longest common subpath is [2,3].

Example 2:

Input: n = 3, paths = [[0],[1],[2]]
Output: 0
Explanation: There is no common subpath shared by the three paths.

Example 3:

Input: n = 5, paths = [[0,1,2,3,4],
                       [4,3,2,1,0]]
Output: 1
Explanation: The possible longest common subpaths are [0], [1], [2],
[3], and [4]. All have a length of 1.

 

Constraints:

	• 1 <= n <= 10^5

	• m == paths.length

	• 2 <= m <= 10^5

	• sum(paths[i].length) <= 10^5

	• 0 <= paths[i][j] < n

• The same city is not listed multiple times consecutively in
paths[i].
"""

class Solution:
    def longestCommonSubpath(self, n: int, paths: list[list[int]]) -> int:
        M1, M2 = 10**9 + 7, 10**9 + 9
        B1, B2 = 911382323, 972663749
        paths = sorted(paths, key=len)
        hi = len(paths[0])
        maxlen = max(len(p) for p in paths)
        pow1 = [1] * (maxlen + 1)
        pow2 = [1] * (maxlen + 1)
        for i in range(1, maxlen + 1):
            pow1[i] = pow1[i - 1] * B1 % M1
            pow2[i] = pow2[i - 1] * B2 % M2

        def check(L):
            if L == 0:
                return True
            common = None
            for p in paths:
                if len(p) < L:
                    return False
                h1 = h2 = 0
                for i in range(L):
                    v = p[i] + 1
                    h1 = (h1 * B1 + v) % M1
                    h2 = (h2 * B2 + v) % M2
                cur = {(h1, h2)}
                for i in range(L, len(p)):
                    h1 = ((h1 - (p[i - L] + 1) * pow1[L - 1]) * B1 + p[i] + 1) % M1
                    h2 = ((h2 - (p[i - L] + 1) * pow2[L - 1]) * B2 + p[i] + 1) % M2
                    cur.add((h1, h2))
                if common is None:
                    common = cur
                else:
                    common &= cur
                    if not common:
                        return False
            return bool(common)

        lo = 0
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
