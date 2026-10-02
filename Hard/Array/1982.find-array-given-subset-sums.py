"""
1982. Find Array Given Subset Sums
Difficulty: Hard
https://leetcode.com/problems/find-array-given-subset-sums/

──────────────────────────────────────────────────

You are given an integer n representing the length of an unknown
array that you are trying to recover. You are also given an array sums
containing the values of all 2^n subset sums of the unknown array (in
no particular order).

Return the array ans of length n representing the unknown array. If
multiple answers exist, return any of them.

An array sub is a subset of an array arr if sub can be obtained from
arr by deleting some (possibly zero or all) elements of arr. The sum
of the elements in sub is one possible subset sum of arr. The sum of
an empty array is considered to be 0.

Note: Test cases are generated such that there will always be at
least one correct answer.

 

Example 1:

Input: n = 3, sums = [-3,-2,-1,0,0,1,2,3]
Output: [1,2,-3]
Explanation: [1,2,-3] is able to achieve the given subset sums:
- []: sum is 0
- [1]: sum is 1
- [2]: sum is 2
- [1,2]: sum is 3
- [-3]: sum is -3
- [1,-3]: sum is -2
- [2,-3]: sum is -1
- [1,2,-3]: sum is 0
Note that any permutation of [1,2,-3] and also any permutation of
[-1,-2,3] will also be accepted.

Example 2:

Input: n = 2, sums = [0,0,0,0]
Output: [0,0]
Explanation: The only correct answer is [0,0].

Example 3:

Input: n = 4, sums = [0,0,5,5,4,-1,4,9,9,-1,4,3,4,8,3,8]
Output: [0,-1,4,5]
Explanation: [0,-1,4,5] is able to achieve the given subset sums.

 

Constraints:

	• 1 <= n <= 15

	• sums.length == 2^n

	• -10^4 <= sums[i] <= 10^4
"""

from collections import Counter

class Solution:
    def recoverArray(self, n: int, sums: list[int]) -> list[int]:
        mn = min(sums)
        vals = sorted(s - mn for s in sums)

        def rec(T):
            if len(T) == 1:
                return []
            if T[0] == T[-1]:
                return [0] * (len(T).bit_length() - 1)
            d = T[0]
            for v in T:
                if v > 0:
                    d = v
                    break
            cnt = Counter(T)
            rest = []
            for v in T:
                if cnt[v] > 0:
                    rest.append(v)
                    cnt[v] -= 1
                    cnt[v + d] -= 1
            return rec(rest) + [d]

        b = rec(vals)
        need = -mn
        neg = 0
        for i in range(1 << len(b)):
            s = 0
            for j in range(len(b)):
                if i >> j & 1:
                    s += b[j]
            if s == need:
                neg = i
                break
        return [-b[i] if neg >> i & 1 else b[i] for i in range(len(b))]

