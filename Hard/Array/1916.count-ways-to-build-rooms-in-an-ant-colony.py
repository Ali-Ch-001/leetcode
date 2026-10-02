"""
1916. Count Ways to Build Rooms in an Ant Colony
Difficulty: Hard
https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/

──────────────────────────────────────────────────

You are an ant tasked with adding n new rooms numbered 0 to n-1 to
your colony. You are given the expansion plan as a 0-indexed integer
array of length n, prevRoom, where prevRoom[i] indicates that you must
build room prevRoom[i] before building room i, and these two rooms
must be connected directly. Room 0 is already built, so prevRoom[0] =
-1. The expansion plan is given such that once all the rooms are
built, every room will be reachable from room 0.



You can only build one room at a time, and you can travel freely
between rooms you have already built only if they are connected. You
can choose to build any room as long as its previous room is already
built.



Return the number of different orders you can build all the rooms in.
Since the answer may be large, return it modulo 10^9 + 7.



 



Example 1:




Input: prevRoom = [-1,0,1]
Output: 1
Explanation: There is only one way to build the additional rooms: 0
&rarr; 1 &rarr; 2



Example 2:





Input: prevRoom = [-1,0,0,1,2]
Output: 6
Explanation:
The 6 ways are:
0 &rarr; 1 &rarr; 3 &rarr; 2 &rarr; 4
0 &rarr; 2 &rarr; 4 &rarr; 1 &rarr; 3
0 &rarr; 1 &rarr; 2 &rarr; 3 &rarr; 4
0 &rarr; 1 &rarr; 2 &rarr; 4 &rarr; 3
0 &rarr; 2 &rarr; 1 &rarr; 3 &rarr; 4
0 &rarr; 2 &rarr; 1 &rarr; 4 &rarr; 3


 


Constraints:




	• n == prevRoom.length

	• 2 <= n <= 10^5

	• prevRoom[0] == -1

	• 0 <= prevRoom[i] < n for all 1 <= i < n

	• Every room is reachable from room 0 once all the rooms are built.
"""

MOD = 10**9 + 7

from typing import List


class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        n = len(prevRoom)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[prevRoom[i]].append(i)
        size = [1] * n
        order = []
        stack = [0]
        while stack:
            u = stack.pop()
            order.append(u)
            for v in children[u]:
                stack.append(v)
        for u in reversed(order):
            for v in children[u]:
                size[u] += size[v]
        prod = 1
        for s in size:
            prod = prod * s % MOD
        fact = 1
        for i in range(2, n + 1):
            fact = fact * i % MOD
        return fact * pow(prod, MOD - 2, MOD) % MOD
