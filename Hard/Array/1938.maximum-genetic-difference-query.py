"""
1938. Maximum Genetic Difference Query
Difficulty: Hard
https://leetcode.com/problems/maximum-genetic-difference-query/

──────────────────────────────────────────────────

There is a rooted tree consisting of n nodes numbered 0 to n - 1.
Each node's number denotes its unique genetic value (i.e. the genetic
value of node x is x). The genetic difference between two genetic
values is defined as the bitwise-XOR of their values. You are given
the integer array parents, where parents[i] is the parent for node i.
If node x is the root of the tree, then parents[x] == -1.

You are also given the array queries where queries[i] = [nodei,
vali]. For each query i, find the maximum genetic difference between
vali and pi, where pi is the genetic value of any node that is on the
path between nodei and the root (including nodei and the root). More
formally, you want to maximize vali XOR pi.

Return an array ans where ans[i] is the answer to the i^th query.

 

Example 1:

Input: parents = [-1,0,1,1], queries = [[0,2],[3,2],[2,5]]
Output: [2,3,7]
Explanation: The queries are processed as follows:
- [0,2]: The node with the maximum genetic difference is 0, with a
difference of 2 XOR 0 = 2.
- [3,2]: The node with the maximum genetic difference is 1, with a
difference of 2 XOR 1 = 3.
- [2,5]: The node with the maximum genetic difference is 2, with a
difference of 5 XOR 2 = 7.

Example 2:

Input: parents = [3,7,-1,2,0,7,0,2], queries = [[4,6],[1,15],[0,5]]
Output: [6,14,7]
Explanation: The queries are processed as follows:
- [4,6]: The node with the maximum genetic difference is 0, with a
difference of 6 XOR 0 = 6.
- [1,15]: The node with the maximum genetic difference is 1, with a
difference of 15 XOR 1 = 14.
- [0,5]: The node with the maximum genetic difference is 2, with a
difference of 5 XOR 2 = 7.

 

Constraints:

	• 2 <= parents.length <= 10^5

• 0 <= parents[i] <= parents.length - 1 for every node i that is not
the root.

	• parents[root] == -1

	• 1 <= queries.length <= 3 * 10^4

	• 0 <= nodei <= parents.length - 1

	• 0 <= vali <= 2 * 10^5
"""

class Solution:
    def maxGeneticDifference(self, parents: list[int], queries: list[list[int]]) -> list[int]:
        n = len(parents)
        root = -1
        children = [[] for _ in range(n)]
        for i, p in enumerate(parents):
            if p == -1:
                root = i
            else:
                children[p].append(i)
        qat = [[] for _ in range(n)]
        for qi, (node, val) in enumerate(queries):
            qat[node].append((val, qi))
        ans = [0] * len(queries)
        trie = [[0, 0, 0]]
        BITS = 18

        def insert(x):
            node = 0
            for b in range(BITS, -1, -1):
                bit = (x >> b) & 1
                nxt = trie[node][bit]
                if nxt == 0:
                    trie.append([0, 0, 0])
                    nxt = len(trie) - 1
                    trie[node][bit] = nxt
                node = nxt
                trie[node][2] += 1

        def remove(x):
            node = 0
            for b in range(BITS, -1, -1):
                node = trie[node][(x >> b) & 1]
                trie[node][2] -= 1

        def query(x):
            node = 0
            res = 0
            for b in range(BITS, -1, -1):
                bit = (x >> b) & 1
                nxt = trie[node][1 - bit]
                if nxt and trie[nxt][2] > 0:
                    res |= 1 << b
                    node = nxt
                else:
                    node = trie[node][bit]
            return res

        stack = [(root, False)]
        while stack:
            node, exiting = stack.pop()
            if exiting:
                remove(node)
            else:
                insert(node)
                for val, qi in qat[node]:
                    ans[qi] = query(val)
                stack.append((node, True))
                for c in children[node]:
                    stack.append((c, False))
        return ans
