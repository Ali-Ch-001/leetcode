"""
1054. Distant Barcodes
Difficulty: Medium
https://leetcode.com/problems/distant-barcodes/

──────────────────────────────────────────────────

In a warehouse, there is a row of barcodes, where the i^th barcode is
barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal.
You may return any answer, and it is guaranteed an answer exists.

 

Example 1:

Input: barcodes = [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]

Example 2:

Input: barcodes = [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,1,2,1,2]

 

Constraints:

	• 1 <= barcodes.length <= 10000

	• 1 <= barcodes[i] <= 10000
"""

class Solution:
    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
        from collections import Counter
        n = len(barcodes)
        counts = Counter(barcodes)
        res = [0] * n
        idx = 0
        for val, cnt in counts.most_common():
            for _ in range(cnt):
                res[idx] = val
                idx += 2
                if idx >= n:
                    idx = 1
        return res
