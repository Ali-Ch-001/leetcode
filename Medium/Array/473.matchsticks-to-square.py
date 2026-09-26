"""
473. Matchsticks to Square
Difficulty: Medium
https://leetcode.com/problems/matchsticks-to-square/

──────────────────────────────────────────────────

You are given an integer array matchsticks where matchsticks[i] is
the length of the i^th matchstick. You want to use all the matchsticks
to make one square. You should not break any stick, but you can link
them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

 

Example 1:

Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the
square came two sticks with length 1.

Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the
matchsticks.

 

Constraints:

	• 1 <= matchsticks.length <= 15

	• 1 <= matchsticks[i] <= 10^8
"""

class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        total = sum(matchsticks)
        if total % 4:
            return False
        side = total // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > side:
            return False
        sides = [0, 0, 0, 0]

        def backtrack(index: int) -> bool:
            if index == len(matchsticks):
                return True
            for i in range(4):
                if sides[i] + matchsticks[index] <= side:
                    sides[i] += matchsticks[index]
                    if backtrack(index + 1):
                        return True
                    sides[i] -= matchsticks[index]
                if sides[i] == 0:
                    break
            return False

        return backtrack(0)
