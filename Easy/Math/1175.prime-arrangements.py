"""
1175. Prime Arrangements
Difficulty: Easy
https://leetcode.com/problems/prime-arrangements/

──────────────────────────────────────────────────

Return the number of permutations of 1 to n so that prime numbers are
at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1,
and cannot be written as a product of two positive integers both
smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but
[5,2,3,4,1] is not because the prime number 5 is at index 1.

Example 2:

Input: n = 100
Output: 682289015

 

Constraints:

	• 1 <= n <= 100
"""

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n < 2:
            return 1
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        p = sum(sieve)
        ans = 1
        for x in range(2, p + 1):
            ans = ans * x % MOD
        for x in range(2, n - p + 1):
            ans = ans * x % MOD
        return ans
        
