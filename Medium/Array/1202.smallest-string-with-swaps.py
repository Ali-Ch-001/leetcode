"""
1202. Smallest String With Swaps
Difficulty: Medium
https://leetcode.com/problems/smallest-string-with-swaps/

──────────────────────────────────────────────────

You are given a string s, and an array of pairs of indices in the
string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of
the string.

You can swap the characters at any pair of indices in the given pairs
any number of times.

Return the lexicographically smallest string that s can be changed to
after using the swaps.

 

Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"

Example 2:

Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"

Example 3:

Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination: 
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"

 

Constraints:

	• 1 <= s.length <= 10^5

	• 0 <= pairs.length <= 10^5

	• 0 <= pairs[i][0], pairs[i][1] < s.length

	• s only contains lower case English letters.
"""

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        n = len(s)
        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in pairs:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        comps: dict[int, list[int]] = {}
        for i in range(n):
            comps.setdefault(find(i), []).append(i)

        res = list(s)
        for idxs in comps.values():
            chars = sorted(s[i] for i in idxs)
            for i, ch in zip(sorted(idxs), chars):
                res[i] = ch
        return "".join(res)
        
