"""
1203. Sort Items by Groups Respecting Dependencies
Difficulty: Hard
https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

──────────────────────────────────────────────────

There are n items each belonging to zero or one of m groups where
group[i] is the group that the i-th item belongs to and it's equal to
-1 if the i-th item belongs to no group. The items and the groups are
zero indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

• The items that belong to the same group are next to each other in
the sorted list.

• There are some relations between these items where beforeItems[i]
is a list containing all the items that should come before the i-th
item in the sorted array (to the left of the i-th item).

Return any solution if there is more than one solution and return an
empty list if there is no solution.

 

Example 1:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems =
[[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]

Example 2:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems =
[[],[6],[5],[6],[3],[],[4],[]]
Output: []
Explanation: This is the same as example 1 except that 4 needs to be
before 6 in the sorted list.

 

Constraints:

	• 1 <= m <= n <= 3 * 10^4

	• group.length == beforeItems.length == n

	• -1 <= group[i] <= m - 1

	• 0 <= beforeItems[i].length <= n - 1

	• 0 <= beforeItems[i][j] <= n - 1

	• i != beforeItems[i][j]

	• beforeItems[i] does not contain duplicates elements.
"""

from collections import deque, defaultdict

class Solution:
    def sortItems(self, n: int, m: int, group: list[int], beforeItems: list[list[int]]) -> list[int]:
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        item_adj = [[] for _ in range(n)]
        item_indeg = [0] * n
        grp_adj = [[] for _ in range(m)]
        grp_indeg = [0] * m

        for i in range(n):
            for b in beforeItems[i]:
                item_adj[b].append(i)
                item_indeg[i] += 1
                if group[b] != group[i]:
                    grp_adj[group[b]].append(group[i])
                    grp_indeg[group[i]] += 1

        q = deque(g for g in range(m) if grp_indeg[g] == 0)
        grp_order = []
        while q:
            g = q.popleft()
            grp_order.append(g)
            for ng in grp_adj[g]:
                grp_indeg[ng] -= 1
                if grp_indeg[ng] == 0:
                    q.append(ng)
        if len(grp_order) != m:
            return []

        q = deque(i for i in range(n) if item_indeg[i] == 0)
        item_order = []
        while q:
            i = q.popleft()
            item_order.append(i)
            for ni in item_adj[i]:
                item_indeg[ni] -= 1
                if item_indeg[ni] == 0:
                    q.append(ni)
        if len(item_order) != n:
            return []

        bucket = defaultdict(list)
        for i in item_order:
            bucket[group[i]].append(i)
        res = []
        for g in grp_order:
            res.extend(bucket[g])
        return res
        
