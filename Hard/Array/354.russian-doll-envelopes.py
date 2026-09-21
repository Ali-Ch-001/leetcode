"""
354. Russian Doll Envelopes
Difficulty: Hard
https://leetcode.com/problems/russian-doll-envelopes/

──────────────────────────────────────────────────

You are given a 2D array of integers envelopes where envelopes[i] =
[wi, hi] represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and
height of one envelope are greater than the other envelope's width and
height.

Return the maximum number of envelopes you can Russian doll (i.e.,
put one inside the other).

Note: You cannot rotate an envelope.

 

Example 1:

Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is
3 ([2,3] => [5,4] => [6,7]).

Example 2:

Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1

 

Constraints:

	• 1 <= envelopes.length <= 10^5

	• envelopes[i].length == 2

	• 1 <= wi, hi <= 10^5
"""

import bisect


class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda pair: (pair[0], -pair[1]))
        tails = []
        for _, height in envelopes:
            index = bisect.bisect_left(tails, height)
            if index == len(tails):
                tails.append(height)
            else:
                tails[index] = height
        return len(tails)
