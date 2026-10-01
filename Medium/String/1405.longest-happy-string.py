"""
1405. Longest Happy String
Difficulty: Medium
https://leetcode.com/problems/longest-happy-string/

──────────────────────────────────────────────────

A string s is called happy if it satisfies the following conditions:

	• s only contains the letters 'a', 'b', and 'c'.

	• s does not contain any of "aaa", "bbb", or "ccc" as a substring.

	• s contains at most a occurrences of the letter 'a'.

	• s contains at most b occurrences of the letter 'b'.

	• s contains at most c occurrences of the letter 'c'.

Given three integers a, b, and c, return the longest possible happy
string. If there are multiple longest happy strings, return any of
them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.

Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.

 

Constraints:

	• 0 <= a, b, c <= 100

	• a + b + c > 0
"""

import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [(-cnt, ch) for cnt, ch in ((a, 'a'), (b, 'b'), (c, 'c')) if cnt > 0]
        heapq.heapify(heap)
        res = []
        while heap:
            neg, ch = heapq.heappop(heap)
            if len(res) >= 2 and res[-1] == ch and res[-2] == ch:
                if not heap:
                    break
                neg2, ch2 = heapq.heappop(heap)
                res.append(ch2)
                if neg2 + 1 < 0:
                    heapq.heappush(heap, (neg2 + 1, ch2))
                heapq.heappush(heap, (neg, ch))
            else:
                res.append(ch)
                if neg + 1 < 0:
                    heapq.heappush(heap, (neg + 1, ch))
        return ''.join(res)

