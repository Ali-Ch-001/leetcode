"""
1900. The Earliest and Latest Rounds Where Players Compete
Difficulty: Hard
https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/

──────────────────────────────────────────────────

There is a tournament where n players are participating. The players
are standing in a single row and are numbered from 1 to n based on
their initial standing position (player 1 is the first player in the
row, player 2 is the second player in the row, etc.).

The tournament consists of multiple rounds (starting from round
number 1). In each round, the i^th player from the front of the row
competes against the i^th player from the end of the row, and the
winner advances to the next round. When the number of players is odd
for the current round, the player in the middle automatically advances
to the next round.

	• For example, if the row consists of players 1, 2, 4, 6, 7

	
		• Player 1 competes against player 7.

		• Player 2 competes against player 6.

		• Player 4 automatically advances to the next round.

	
	

After each round is over, the winners are lined back up in the row
based on the original ordering assigned to them initially (ascending
order).

The players numbered firstPlayer and secondPlayer are the best in the
tournament. They can win against any other player before they compete
against each other. If any two other players compete against each
other, either of them might win, and thus you may choose the outcome
of this round.

Given the integers n, firstPlayer, and secondPlayer, return an
integer array containing two values, the earliest possible round
number and the latest possible round number in which these two players
will compete against each other, respectively.

 

Example 1:

Input: n = 11, firstPlayer = 2, secondPlayer = 4
Output: [3,4]
Explanation:
One possible scenario which leads to the earliest round number:
First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
Second round: 2, 3, 4, 5, 6, 11
Third round: 2, 3, 4
One possible scenario which leads to the latest round number:
First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
Second round: 1, 2, 3, 4, 5, 6
Third round: 1, 2, 4
Fourth round: 2, 4

Example 2:

Input: n = 5, firstPlayer = 1, secondPlayer = 5
Output: [1,1]
Explanation: The players numbered 1 and 5 compete in the first round.
There is no way to make them compete in any other round.

 

Constraints:

	• 2 <= n <= 28

	• 1 <= firstPlayer < secondPlayer <= n
"""

from functools import cache


class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> list[int]:
        @cache
        def solve(n, f, s):
            if f + s == n + 1:
                return (1, 1)

            def region(p):
                if p < f:
                    return 0
                if p == f:
                    return 1
                if p < s:
                    return 2
                if p == s:
                    return 3
                return 4

            options = {(0, 0)}
            for i in range(1, n // 2 + 1):
                x, y = i, n + 1 - i
                rx, ry = region(x), region(y)
                if rx == 1 or ry == 1 or rx == 3 or ry == 3:
                    contrib = [(0, 0)]
                else:
                    pair_regions = {rx, ry}
                    if pair_regions == {0}:
                        contrib = [(1, 0)]
                    elif pair_regions == {2}:
                        contrib = [(0, 1)]
                    elif pair_regions == {0, 2}:
                        contrib = [(1, 0), (0, 1)]
                    elif pair_regions == {0, 4}:
                        contrib = [(1, 0), (0, 0)]
                    elif pair_regions == {2, 4}:
                        contrib = [(0, 1), (0, 0)]
                    else:
                        contrib = [(0, 0)]
                options = {(a + da, b + db) for a, b in options for da, db in contrib}

            if n % 2 == 1:
                m = n // 2 + 1
                if m < f:
                    options = {(a + 1, b) for a, b in options}
                elif f < m < s:
                    options = {(a, b + 1) for a, b in options}

            n2 = (n + 1) // 2
            best = worst = None
            for a, b in options:
                f2, s2 = a + 1, a + b + 2
                if s2 > n2:
                    continue
                e, l = solve(n2, f2, s2)
                e += 1
                l += 1
                best = e if best is None else min(best, e)
                worst = l if worst is None else max(worst, l)
            return (best, worst)

        return list(solve(n, firstPlayer, secondPlayer))
