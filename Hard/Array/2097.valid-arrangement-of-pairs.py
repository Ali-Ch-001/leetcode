"""
2097. Valid Arrangement of Pairs
Difficulty: Hard
https://leetcode.com/problems/valid-arrangement-of-pairs/

──────────────────────────────────────────────────

You are given a 0-indexed 2D integer array pairs where pairs[i] =
[starti, endi]. An arrangement of pairs is valid if for every index i
where 1 <= i < pairs.length, we have endi-1 == starti.

Return any valid arrangement of pairs.

Note: The inputs will be generated such that there exists a valid
arrangement of pairs.

 

Example 1:

Input: pairs = [[5,1],[4,5],[11,9],[9,4]]
Output: [[11,9],[9,4],[4,5],[5,1]]
Explanation:
This is a valid arrangement since endi-1 always equals starti.
end0 = 9 == 9 = start1 
end1 = 4 == 4 = start2
end2 = 5 == 5 = start3

Example 2:

Input: pairs = [[1,3],[3,2],[2,1]]
Output: [[1,3],[3,2],[2,1]]
Explanation:
This is a valid arrangement since endi-1 always equals starti.
end0 = 3 == 3 = start1
end1 = 2 == 2 = start2
The arrangements [[2,1],[1,3],[3,2]] and [[3,2],[2,1],[1,3]] are also
valid.

Example 3:

Input: pairs = [[1,2],[1,3],[2,1]]
Output: [[1,2],[2,1],[1,3]]
Explanation:
This is a valid arrangement since endi-1 always equals starti.
end0 = 2 == 2 = start1
end1 = 1 == 1 = start2

 

Constraints:

	• 1 <= pairs.length <= 10^5

	• pairs[i].length == 2

	• 0 <= starti, endi <= 10^9

	• starti != endi

	• No two pairs are exactly the same.

	• There exists a valid arrangement of pairs.
"""

from collections import Counter, defaultdict


class Solution:
    def validArrangement(self, pairs: list[list[int]]) -> list[list[int]]:
        adj = defaultdict(list)
        outd = Counter()
        ind = Counter()
        for a, b in pairs:
            adj[a].append(b)
            outd[a] += 1
            ind[b] += 1
        start = pairs[0][0]
        for node in adj:
            if outd[node] - ind[node] == 1:
                start = node
                break
        stack = [start]
        path = []
        while stack:
            u = stack[-1]
            if adj[u]:
                stack.append(adj[u].pop())
            else:
                path.append(stack.pop())
        path.reverse()
        return [[path[i], path[i + 1]] for i in range(len(path) - 1)]
