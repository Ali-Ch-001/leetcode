"""
600. Non-negative Integers without Consecutive Ones
Difficulty: Hard
https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/

──────────────────────────────────────────────────

Given a positive integer n, return the number of the integers in the
range [0, n] whose binary representations do not contain consecutive
ones.

 

Example 1:

Input: n = 5
Output: 5
Explanation:
Here are the non-negative integers <= 5 with their corresponding
binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones)
and the other 5 satisfy the rule.

Example 2:

Input: n = 1
Output: 2

Example 3:

Input: n = 2
Output: 3

 

Constraints:

	• 1 <= n <= 10^9
"""

class Solution:
    def findIntegers(self, n: int) -> int:
        bits = bin(n)[2:]
        length = len(bits)
        fib = [0] * (length + 2)
        fib[0] = 1
        fib[1] = 2
        for i in range(2, length + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        count = 0
        previous = "0"
        for i, ch in enumerate(bits):
            if ch == "1":
                count += fib[length - i - 1]
                if previous == "1":
                    return count
            previous = ch
        return count + 1
