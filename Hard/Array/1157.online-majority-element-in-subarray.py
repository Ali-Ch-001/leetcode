"""
1157. Online Majority Element In Subarray
Difficulty: Hard
https://leetcode.com/problems/online-majority-element-in-subarray/

──────────────────────────────────────────────────

Design a data structure that efficiently finds the majority element
of a given subarray.

The majority element of a subarray is an element that occurs
threshold times or more in the subarray.

Implementing the MajorityChecker class:

• MajorityChecker(int[] arr) Initializes the instance of the class
with the given array arr.

• int query(int left, int right, int threshold) returns the element
in the subarray arr[left...right] that occurs at least threshold
times, or -1 if no such element exists.

 

Example 1:

Input
["MajorityChecker", "query", "query", "query"]
[[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
Output
[null, 1, -1, 2]

Explanation
MajorityChecker majorityChecker = new MajorityChecker([1, 1, 2, 2, 1,
1]);
majorityChecker.query(0, 5, 4); // return 1
majorityChecker.query(0, 3, 3); // return -1
majorityChecker.query(2, 3, 2); // return 2

 

Constraints:

	• 1 <= arr.length <= 2 * 10^4

	• 1 <= arr[i] <= 2 * 10^4

	• 0 <= left <= right < arr.length

	• threshold <= right - left + 1

	• 2 * threshold > right - left + 1

	• At most 10^4 calls will be made to query.
"""

import bisect
from collections import defaultdict


class MajorityChecker:

    def __init__(self, arr: list[int]):
        self.pos = defaultdict(list)
        for i, v in enumerate(arr):
            self.pos[v].append(i)
        n = len(arr)
        size = 1
        while size < n:
            size *= 2
        self.size = size
        self.cand = [0] * (2 * size)
        self.cnt = [0] * (2 * size)
        for i, v in enumerate(arr):
            self.cand[size + i] = v
            self.cnt[size + i] = 1
        for i in range(size - 1, 0, -1):
            self.cand[i], self.cnt[i] = self._merge(
                (self.cand[2 * i], self.cnt[2 * i]),
                (self.cand[2 * i + 1], self.cnt[2 * i + 1]),
            )

    @staticmethod
    def _merge(a, b):
        ca, na = a
        cb, nb = b
        if ca == cb:
            return ca, na + nb
        if na > nb:
            return ca, na - nb
        if nb > na:
            return cb, nb - na
        return 0, 0

    def query(self, left: int, right: int, threshold: int) -> int:
        l = left + self.size
        r = right + self.size
        res = (0, 0)
        while l <= r:
            if l % 2 == 1:
                res = self._merge(res, (self.cand[l], self.cnt[l]))
                l += 1
            if r % 2 == 0:
                res = self._merge(res, (self.cand[r], self.cnt[r]))
                r -= 1
            l //= 2
            r //= 2
        cand = res[0]
        if cand == 0:
            return -1
        lst = self.pos[cand]
        count = bisect.bisect_right(lst, right) - bisect.bisect_left(lst, left)
        return cand if count >= threshold else -1



# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
