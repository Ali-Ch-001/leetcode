"""
1399. Count Largest Group
Difficulty: Easy
https://leetcode.com/problems/count-largest-group/

──────────────────────────────────────────────────

You are given an integer n.

We need to group the numbers from 1 to n according to the sum of its
digits. For example, the numbers 14 and 5 belong to the same group,
whereas 13 and 3 belong to different groups.

Return the number of groups that have the largest size, i.e. the
maximum number of elements.

 

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according
sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.

Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.

 

Constraints:

	• 1 <= n <= 10^4
"""

class Solution:
    def countLargestGroup(self, n: int) -> int:
        counts = {}
        best = 0
        for x in range(1, n + 1):
            s = 0
            y = x
            while y:
                s += y % 10
                y //= 10
            counts[s] = counts.get(s, 0) + 1
            if counts[s] > best:
                best = counts[s]
        return sum(1 for v in counts.values() if v == best)

