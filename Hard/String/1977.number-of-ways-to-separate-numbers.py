"""
1977. Number of Ways to Separate Numbers
Difficulty: Hard
https://leetcode.com/problems/number-of-ways-to-separate-numbers/

──────────────────────────────────────────────────

You wrote down many positive integers in a string called num.
However, you realized that you forgot to add commas to seperate the
different numbers. You remember that the list of integers was
non-decreasing and that no integer had leading zeros.

Return the number of possible lists of integers that you could have
written down to get the string num. Since the answer may be large,
return it modulo 10^9 + 7.

 

Example 1:

Input: num = "327"
Output: 2
Explanation: You could have written down the numbers:
3, 27
327

Example 2:

Input: num = "094"
Output: 0
Explanation: No numbers can have leading zeros and all numbers must
be positive.

Example 3:

Input: num = "0"
Output: 0
Explanation: No numbers can have leading zeros and all numbers must
be positive.

 

Constraints:

	• 1 <= num.length <= 3500

	• num consists of digits '0' through '9'.
"""

from array import array

class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MOD = 10**9 + 7
        n = len(num)
        if num[0] == '0':
            return 0
        W = n + 1
        z = bytes(4 * W)
        pre = [array('i', z) for _ in range(W)]
        P = [0] * (n + 1)
        for j in range(1, n + 1):
            d = j
            lim = n - d
            if 2 * j <= n:
                P[lim] = 0
                for a in range(lim - 1, -1, -1):
                    P[a] = P[a + 1] + 1 if num[a] == num[a + d] else 0
            row = pre[j]
            row[j] = (row[j - 1] + 1) % MOD
            hi = 2 * j
            if hi > n + 1:
                hi = n + 1
            for i in range(j + 1, hi):
                x = i - j
                row = pre[i]
                if num[x] != '0':
                    row[j] = (row[j - 1] + pre[x][x]) % MOD
                else:
                    row[j] = row[j - 1]
            lo = hi if hi > j + 1 else j + 1
            for i in range(lo, n + 1):
                x = i - j
                row = pre[i]
                if num[x] != '0':
                    cx = pre[x]
                    dp = cx[j]
                    a = x - j
                    if num[a] != '0':
                        p = P[a]
                        if p < j and num[a + p] > num[x + p]:
                            dp -= cx[j] - cx[j - 1]
                    row[j] = (row[j - 1] + dp) % MOD
                else:
                    row[j] = row[j - 1]
        return pre[n][n] % MOD

