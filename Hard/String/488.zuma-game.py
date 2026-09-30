"""
488. Zuma Game
Difficulty: Hard
https://leetcode.com/problems/zuma-game/

──────────────────────────────────────────────────

You are playing a variation of the game Zuma.

In this variation of Zuma, there is a single row of colored balls on
a board, where each ball can be colored red 'R', yellow 'Y', blue 'B',
green 'G', or white 'W'. You also have several colored balls in your
hand.

Your goal is to clear all of the balls from the board. On each turn:

• Pick any ball from your hand and insert it in between two balls in
the row or on either end of the row.

• If there is a group of three or more consecutive balls of the same
color, remove the group of balls from the board.
	
• If this removal causes more groups of three or more of the same
color to form, then continue removing each group until there are none
left.

	
	

	• If there are no more balls on the board, then you win the game.

• Repeat this process until you either win or do not have any more
balls in your hand.

Given a string board, representing the row of balls on the board, and
a string hand, representing the balls in your hand, return the minimum
number of balls you have to insert to clear all the balls from the
board. If you cannot clear all the balls from the board using the
balls in your hand, return -1.

 

Example 1:

Input: board = "WRRBBW", hand = "RB"
Output: -1
Explanation: It is impossible to clear all the balls. The best you
can do is:
- Insert 'R' so the board becomes WRRRBBW. WRRRBBW -> WBBW.
- Insert 'B' so the board becomes WBBBW. WBBBW -> WW.
There are still balls remaining on the board, and you are out of
balls to insert.

Example 2:

Input: board = "WWRRBBWW", hand = "WRBRW"
Output: 2
Explanation: To make the board empty:
- Insert 'R' so the board becomes WWRRRBBWW. WWRRRBBWW -> WWBBWW.
- Insert 'B' so the board becomes WWBBBWW. WWBBBWW -> WWWW -> empty.
2 balls from your hand were needed to clear the board.

Example 3:

Input: board = "G", hand = "GGGGG"
Output: 2
Explanation: To make the board empty:
- Insert 'G' so the board becomes GG.
- Insert 'G' so the board becomes GGG. GGG -> empty.
2 balls from your hand were needed to clear the board.

 

Constraints:

	• 1 <= board.length <= 16

	• 1 <= hand.length <= 5

• board and hand consist of the characters 'R', 'Y', 'B', 'G', and
'W'.

• The initial row of balls on the board will not have any groups of
three or more consecutive balls of the same color.
"""

import re
from collections import deque
from functools import lru_cache

PATTERN = re.compile(r"(.)\1{2,}")


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        @lru_cache(maxsize=None)
        def shrink(state: str) -> str:
            while True:
                cleaned = PATTERN.sub("", state)
                if cleaned == state or not cleaned:
                    return cleaned
                state = cleaned

        @lru_cache(maxsize=None)
        def insert_results(current: str, color: str) -> tuple:
            n = len(current)
            results = []
            seen_local = set()
            for position in range(n + 1):
                candidate = current[:position] + color + current[position:]
                left = current[position - 1] if position else ""
                right = current[position] if position < n else ""
                if left == color:
                    if right == color or (position >= 2 and current[position - 2] == color):
                        candidate = shrink(candidate)
                        if candidate == current:
                            continue
                elif right == color and position + 1 < n and current[position + 1] == color:
                    candidate = shrink(candidate)
                    if candidate == current:
                        continue
                if candidate not in seen_local:
                    seen_local.add(candidate)
                    results.append(candidate)
            return tuple(results)

        hand_cache = {}

        def hand_sets(remaining: str):
            info = hand_cache.get(remaining)
            if info is None:
                colors = set(remaining)
                info = (colors, {c: remaining.count(c) for c in colors})
                hand_cache[remaining] = info
            return info

        start = shrink(board)
        hand_sorted = "".join(sorted(hand))
        queue = deque([(start, hand_sorted, 0)])
        seen = {(start, hand_sorted)}
        push = seen.add
        append = queue.append
        pop = queue.popleft
        while queue:
            current, remaining, steps = pop()
            if not current:
                return steps
            board_colors = set(current)
            dead = False
            for color in board_colors:
                if current.count(color) + remaining.count(color) < 3:
                    dead = True
                    break
            if dead:
                continue
            colors, counts = hand_sets(remaining)
            for color in colors:
                if color not in board_colors and counts[color] < 3:
                    continue
                new_hand = remaining.replace(color, "", 1)
                for new_board in insert_results(current, color):
                    state = (new_board, new_hand)
                    if state not in seen:
                        push(state)
                        append((new_board, new_hand, steps + 1))
        return -1
