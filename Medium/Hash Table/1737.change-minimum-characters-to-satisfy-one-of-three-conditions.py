"""
1737. Change Minimum Characters to Satisfy One of Three Conditions
Difficulty: Medium
https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/

──────────────────────────────────────────────────

You are given two strings a and b that consist of lowercase letters.
In one operation, you can change any character in a or b to any
lowercase letter.

Your goal is to satisfy one of the following three conditions:

• Every letter in a is strictly less than every letter in b in the
alphabet.

• Every letter in b is strictly less than every letter in a in the
alphabet.

	• Both a and b consist of only one distinct letter.

Return the minimum number of operations needed to achieve your goal.

 

Example 1:

Input: a = "aba", b = "caa"
Output: 2
Explanation: Consider the best way to make each condition true:
1) Change b to "ccc" in 2 operations, then every letter in a is less
than every letter in b.
2) Change a to "bbb" and b to "aaa" in 3 operations, then every
letter in b is less than every letter in a.
3) Change a to "aaa" and b to "aaa" in 2 operations, then a and b
consist of one distinct letter.
The best way was done in 2 operations (either condition 1 or
condition 3).

Example 2:

Input: a = "dabadd", b = "cda"
Output: 3
Explanation: The best way is to make condition 1 true by changing b
to "eee".

 

Constraints:

	• 1 <= a.length, b.length <= 10^5

	• a and b consist only of lowercase letters.
"""

class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        ca = [0] * 26
        cb = [0] * 26
        for ch in a:
            ca[ord(ch) - 97] += 1
        for ch in b:
            cb[ord(ch) - 97] += 1
        la, lb = len(a), len(b)

        best = la + lb - max(ca[i] + cb[i] for i in range(26))

        ca_leq = cb_leq = 0
        for x in range(25):
            ca_leq += ca[x]
            cb_leq += cb[x]
            cost = (la - ca_leq) + cb_leq
            if cost < best:
                best = cost
            cost = (lb - cb_leq) + ca_leq
            if cost < best:
                best = cost
        return best
