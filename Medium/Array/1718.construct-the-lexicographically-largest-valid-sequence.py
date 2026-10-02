"""
1718. Construct the Lexicographically Largest Valid Sequence
Difficulty: Medium
https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

──────────────────────────────────────────────────

Given an integer n, find a sequence with elements in the range [1, n]
that satisfies all of the following:

	• The integer 1 occurs once in the sequence.

	• Each integer between 2 and n occurs twice in the sequence.

• For every integer i between 2 and n, the distance between the two
occurrences of i is exactly i.

The distance between two numbers on the sequence, a[i] and a[j], is
the absolute difference of their indices, |j - i|.

Return the lexicographically largest sequence. It is guaranteed that
under the given constraints, there is always a solution.

A sequence a is lexicographically larger than a sequence b (of the
same length) if in the first position where a and b differ, sequence a
has a number greater than the corresponding number in b. For example,
[0,1,9,0] is lexicographically larger than [0,1,5,6] because the first
position they differ is at the third number, and 9 is greater than 5.

 

Example 1:

Input: n = 3
Output: [3,1,2,3,2]
Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is
the lexicographically largest valid sequence.

Example 2:

Input: n = 5
Output: [5,3,1,4,3,5,2,4,2]

 

Constraints:

	• 1 <= n <= 20
"""

class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        length = 2 * n - 1
        res = [0] * length
        used = [False] * (n + 1)

        def backtrack(pos: int) -> bool:
            if pos == length:
                return True
            if res[pos]:
                return backtrack(pos + 1)
            for v in range(n, 0, -1):
                if used[v]:
                    continue
                if v == 1:
                    res[pos] = 1
                    used[1] = True
                    if backtrack(pos + 1):
                        return True
                    res[pos] = 0
                    used[1] = False
                elif pos + v < length and res[pos + v] == 0:
                    res[pos] = res[pos + v] = v
                    used[v] = True
                    if backtrack(pos + 1):
                        return True
                    res[pos] = res[pos + v] = 0
                    used[v] = False
            return False

        backtrack(0)
        return res
