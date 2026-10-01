"""
1606. Find Servers That Handled Most Number of Requests
Difficulty: Hard
https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/

──────────────────────────────────────────────────

You have k servers numbered from 0 to k-1 that are being used to
handle multiple requests simultaneously. Each server has infinite
computational capacity but cannot handle more than one request at a
time. The requests are assigned to servers according to a specific
algorithm:

	• The i^th (0-indexed) request arrives.

• If all servers are busy, the request is dropped (not handled at
all).

• If the (i % k)^th server is available, assign the request to that
server.

• Otherwise, assign the request to the next available server
(wrapping around the list of servers and starting from 0 if
necessary). For example, if the i^th server is busy, try to assign the
request to the (i+1)^th server, then the (i+2)^th server, and so on.

You are given a strictly increasing array arrival of positive
integers, where arrival[i] represents the arrival time of the i^th
request, and another array load, where load[i] represents the load of
the i^th request (the time it takes to complete). Your goal is to find
the busiest server(s). A server is considered busiest if it handled
the most number of requests successfully among all the servers.

Return a list containing the IDs (0-indexed) of the busiest
server(s). You may return the IDs in any order.

 

Example 1:

Input: k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] 
Output: [1] 
Explanation: 
All of the servers start out available.
The first 3 requests are handled by the first 3 servers in order.
Request 3 comes in. Server 0 is busy, so it's assigned to the next
available server, which is 1.
Request 4 comes in. It cannot be handled since all servers are busy,
so it is dropped.
Servers 0 and 2 handled one request each, while server 1 handled two
requests. Hence server 1 is the busiest server.

Example 2:

Input: k = 3, arrival = [1,2,3,4], load = [1,2,1,2]
Output: [0]
Explanation: 
The first 3 requests are handled by first 3 servers.
Request 3 comes in. It is handled by server 0 since the server is
available.
Server 0 handled two requests, while servers 1 and 2 handled one
request each. Hence server 0 is the busiest server.

Example 3:

Input: k = 3, arrival = [1,2,3], load = [10,12,11]
Output: [0,1,2]
Explanation: Each server handles a single request, so they are all
considered the busiest.

 

Constraints:

	• 1 <= k <= 10^5

	• 1 <= arrival.length, load.length <= 10^5

	• arrival.length == load.length

	• 1 <= arrival[i], load[i] <= 10^9

	• arrival is strictly increasing.
"""

import heapq


class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        tree = [0] * (k + 1)
        for i in range(1, k + 1):
            tree[i] += 1
            j = i + (i & -i)
            if j <= k:
                tree[j] += tree[i]

        def add(i: int, delta: int) -> None:
            while i <= k:
                tree[i] += delta
                i += i & -i

        def prefix(i: int) -> int:
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & -i
            return s

        def find_kth(t: int) -> int:
            idx = 0
            bit = 1 << (k.bit_length() - 1)
            while bit:
                nxt = idx + bit
                if nxt <= k and tree[nxt] < t:
                    idx = nxt
                    t -= tree[nxt]
                bit >>= 1
            return idx + 1

        counts = [0] * k
        busy = []
        for i, (a, l) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= a:
                _, s = heapq.heappop(busy)
                add(s + 1, 1)
            total = prefix(k)
            if total == 0:
                continue
            target = i % k
            before = prefix(target)
            if before < total:
                s = find_kth(before + 1)
            else:
                s = find_kth(1)
            s -= 1
            counts[s] += 1
            add(s + 1, -1)
            heapq.heappush(busy, (a + l, s))
        best = max(counts)
        return [i for i, c in enumerate(counts) if c == best]
