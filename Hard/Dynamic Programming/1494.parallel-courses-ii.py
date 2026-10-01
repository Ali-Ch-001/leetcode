"""
1494. Parallel Courses II
Difficulty: Hard
https://leetcode.com/problems/parallel-courses-ii/

──────────────────────────────────────────────────

You are given an integer n, which indicates that there are n courses
labeled from 1 to n. You are also given an array relations where
relations[i] = [prevCoursei, nextCoursei], representing a prerequisite
relationship between course prevCoursei and course nextCoursei: course
prevCoursei has to be taken before course nextCoursei. Also, you are
given the integer k.

In one semester, you can take at most k courses as long as you have
taken all the prerequisites in the previous semesters for the courses
you are taking.

Return the minimum number of semesters needed to take all courses.
The testcases will be generated such that it is possible to take every
course.

 

Example 1:

Input: n = 4, relations = [[2,1],[3,1],[1,4]], k = 2
Output: 3
Explanation: The figure above represents the given graph.
In the first semester, you can take courses 2 and 3.
In the second semester, you can take course 1.
In the third semester, you can take course 4.

Example 2:

Input: n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2
Output: 4
Explanation: The figure above represents the given graph.
In the first semester, you can only take courses 2 and 3 since you
cannot take more than two per semester.
In the second semester, you can take course 4.
In the third semester, you can take course 1.
In the fourth semester, you can take course 5.

 

Constraints:

	• 1 <= n <= 15

	• 1 <= k <= n

	• 0 <= relations.length <= n * (n-1) / 2

	• relations[i].length == 2

	• 1 <= prevCoursei, nextCoursei <= n

	• prevCoursei != nextCoursei

	• All the pairs [prevCoursei, nextCoursei] are unique.

	• The given graph is a directed acyclic graph.
"""

class Solution:
    def minNumberOfSemesters(self, n: int, relations: list[list[int]], k: int) -> int:
        from itertools import combinations

        pre = [0] * n
        for a, b in relations:
            pre[b - 1] |= 1 << (a - 1)
        full = (1 << n) - 1
        INF = float('inf')
        dp = [INF] * (1 << n)
        dp[0] = 0
        combo_mask = {}

        def get_mask(comb):
            s = combo_mask.get(comb)
            if s is None:
                s = 0
                for i in comb:
                    s |= 1 << i
                combo_mask[comb] = s
            return s

        for mask in range(1 << n):
            cur = dp[mask]
            if cur == INF:
                continue
            avail = 0
            for i in range(n):
                if not (mask >> i) & 1 and (pre[i] & mask) == pre[i]:
                    avail |= 1 << i
            if avail == 0:
                continue
            bits = [i for i in range(n) if (avail >> i) & 1]
            if len(bits) <= k:
                nm = mask | avail
                if dp[nm] > cur + 1:
                    dp[nm] = cur + 1
            else:
                for comb in combinations(bits, k):
                    nm = mask | get_mask(comb)
                    if dp[nm] > cur + 1:
                        dp[nm] = cur + 1
        return dp[full]
        
