"""
1397. Find All Good Strings
Difficulty: Hard
https://leetcode.com/problems/find-all-good-strings/

──────────────────────────────────────────────────

Given the strings s1 and s2 of size n and the string evil, return the
number of good strings.

A good string has size n, it is alphabetically greater than or equal
to s1, it is alphabetically smaller than or equal to s2, and it does
not contain the string evil as a substring. Since the answer can be a
huge number, return this modulo 10^9 + 7.

 

Example 1:

Input: n = 2, s1 = "aa", s2 = "da", evil = "b"
Output: 51 
Explanation: There are 25 good strings starting with 'a':
"aa","ac","ad",...,"az". Then there are 25 good strings starting with
'c': "ca","cc","cd",...,"cz" and finally there is one good string
starting with 'd': "da".

Example 2:

Input: n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"
Output: 0 
Explanation: All strings greater than or equal to s1 and smaller than
or equal to s2 start with the prefix "leet", therefore, there is not
any good string.

Example 3:

Input: n = 2, s1 = "gx", s2 = "gz", evil = "x"
Output: 2

 

Constraints:

	• s1.length == n

	• s2.length == n

	• s1 <= s2

	• 1 <= n <= 500

	• 1 <= evil.length <= 50

	• All strings consist of lowercase English letters.
"""

class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        MOD = 10 ** 9 + 7
        m = len(evil)
        fail = [0] * m
        k = 0
        for i in range(1, m):
            while k and evil[i] != evil[k]:
                k = fail[k - 1]
            if evil[i] == evil[k]:
                k += 1
            fail[i] = k
        trans = [[0] * 26 for _ in range(m)]
        for state in range(m):
            for c in range(26):
                ch = chr(97 + c)
                k = state
                while k and evil[k] != ch:
                    k = fail[k - 1]
                if evil[k] == ch:
                    k += 1
                trans[state][c] = k
        agg = []
        for state in range(m):
            counts = {}
            for c in range(26):
                ns = trans[state][c]
                if ns < m:
                    counts[ns] = counts.get(ns, 0) + 1
            agg.append(list(counts.items()))

        def count_leq(s):
            less = [0] * m
            tight_state = 0
            tight_alive = True
            for ch in s:
                ci = ord(ch) - 97
                new_less = [0] * m
                for j, v in enumerate(less):
                    if v:
                        for ns, cnt in agg[j]:
                            new_less[ns] = (new_less[ns] + v * cnt) % MOD
                if tight_alive:
                    row = trans[tight_state]
                    for c in range(ci):
                        ns = row[c]
                        if ns < m:
                            new_less[ns] += 1
                    ns = row[ci]
                    if ns == m:
                        tight_alive = False
                    else:
                        tight_state = ns
                less = new_less
            return (sum(less) + (1 if tight_alive else 0)) % MOD

        ans = (count_leq(s2) - count_leq(s1)) % MOD
        if evil not in s1:
            ans = (ans + 1) % MOD
        return ans
        
