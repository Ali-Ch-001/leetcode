"""
2055. Plates Between Candles
Difficulty: Medium
https://leetcode.com/problems/plates-between-candles/

──────────────────────────────────────────────────

There is a long table with a line of plates and candles arranged on
top of it. You are given a 0-indexed string s consisting of characters
'*' and '|' only, where a '*' represents a plate and a '|' represents
a candle.

You are also given a 0-indexed 2D integer array queries where
queries[i] = [lefti, righti] denotes the substring s[lefti...righti]
(inclusive). For each query, you need to find the number of plates
between candles that are in the substring. A plate is considered
between candles if there is at least one candle to its left and at
least one candle to its right in the substring.

• For example, s = "||**||**|*", and a query [3, 8] denotes the
substring "*||**|". The number of plates between candles in this
substring is 2, as each of the two plates has at least one candle in
the substring to its left and right.

Return an integer array answer where answer[i] is the answer to the
i^th query.

 

Example 1:

Input: s = "**|**|***|", queries = [[2,5],[5,9]]
Output: [2,3]
Explanation:
- queries[0] has two plates between candles.
- queries[1] has three plates between candles.

Example 2:

Input: s = "***|**|*****|**||**|*", queries =
[[1,17],[4,5],[14,17],[5,11],[15,16]]
Output: [9,0,0,0,0]
Explanation:
- queries[0] has nine plates between candles.
- The other queries have zero plates between candles.

 

Constraints:

	• 3 <= s.length <= 10^5

	• s consists of '*' and '|' characters.

	• 1 <= queries.length <= 10^5

	• queries[i].length == 2

	• 0 <= lefti <= righti < s.length
"""

class Solution:
    def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        pre = [0] * (n + 1)
        for i, ch in enumerate(s):
            pre[i + 1] = pre[i] + (ch == '*')
        next_candle = [n] * (n + 1)
        for i in range(n - 1, -1, -1):
            next_candle[i] = i if s[i] == '|' else next_candle[i + 1]
        prev_candle = [-1] * (n + 1)
        for i in range(n):
            prev_candle[i + 1] = i if s[i] == '|' else prev_candle[i]
        ans = []
        for l, r in queries:
            left = next_candle[l]
            right = prev_candle[r + 1]
            if left < right:
                ans.append(pre[right] - pre[left + 1])
            else:
                ans.append(0)
        return ans

