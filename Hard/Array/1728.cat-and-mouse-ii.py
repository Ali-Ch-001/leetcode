"""
1728. Cat and Mouse II
Difficulty: Hard
https://leetcode.com/problems/cat-and-mouse-ii/

──────────────────────────────────────────────────

A game is played by a cat and a mouse named Cat and Mouse.

The environment is represented by a grid of size rows x cols, where
each element is a wall, floor, player (Cat, Mouse), or food.

	• Players are represented by the characters 'C'(Cat),'M'(Mouse).

	• Floors are represented by the character '.' and can be walked on.

	• Walls are represented by the character '#' and cannot be walked on.

	• Food is represented by the character 'F' and can be walked on.

	• There is only one of each character 'C', 'M', and 'F' in grid.

Mouse and Cat play according to the following rules:

	• Mouse moves first, then they take turns to move.

• During each turn, Cat and Mouse can jump in one of the four
directions (left, right, up, down). They cannot jump over the wall nor
outside of the grid.

• catJump, mouseJump are the maximum lengths Cat and Mouse can jump
at a time, respectively. Cat and Mouse can jump less than the maximum
length.

	• Staying in the same position is allowed.

	• Mouse can jump over Cat.

The game can end in 4 ways:

	• If Cat occupies the same position as Mouse, Cat wins.

	• If Cat reaches the food first, Cat wins.

	• If Mouse reaches the food first, Mouse wins.

	• If Mouse cannot get to the food within 1000 turns, Cat wins.

Given a rows x cols matrix grid and two integers catJump and
mouseJump, return true if Mouse can win the game if both Cat and Mouse
play optimally, otherwise return false.

 

Example 1:

Input: grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2
Output: true
Explanation: Cat cannot catch Mouse on its turn nor can it get the
food before Mouse.

Example 2:

Input: grid = ["M.C...F"], catJump = 1, mouseJump = 4
Output: true

Example 3:

Input: grid = ["M.C...F"], catJump = 1, mouseJump = 3
Output: false

 

Constraints:

	• rows == grid.length

	• cols = grid[i].length

	• 1 <= rows, cols <= 8

	• grid[i][j] consist only of characters 'C', 'M', 'F', '.', and '#'.

	• There is only one of each character 'C', 'M', and 'F' in grid.

	• 1 <= catJump, mouseJump <= 8
"""

class Solution:
    def canMouseWin(self, grid: list[str], catJump: int, mouseJump: int) -> bool:
        from collections import deque

        R, C = len(grid), len(grid[0])
        cells = {}
        for r in range(R):
            for c in range(C):
                ch = grid[r][c]
                if ch != '#':
                    cells[(r, c)] = len(cells)
                if ch == 'M':
                    mouse = (r, c)
                elif ch == 'C':
                    cat = (r, c)
                elif ch == 'F':
                    food = (r, c)
        N = len(cells)
        mi, ci, fi = cells[mouse], cells[cat], cells[food]

        def build_moves(jump):
            moves = [[] for _ in range(N)]
            for (r, c), idx in cells.items():
                lst = [idx]
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    for step in range(1, jump + 1):
                        nr, nc = r + dr * step, c + dc * step
                        if not (0 <= nr < R and 0 <= nc < C):
                            break
                        if grid[nr][nc] == '#':
                            break
                        lst.append(cells[(nr, nc)])
                moves[idx] = lst
            return moves

        mouse_moves = build_moves(mouseJump)
        cat_moves = build_moves(catJump)

        mouse_prev = [[] for _ in range(N)]
        for u in range(N):
            for v in mouse_moves[u]:
                mouse_prev[v].append(u)
        cat_prev = [[] for _ in range(N)]
        for u in range(N):
            for v in cat_moves[u]:
                cat_prev[v].append(u)

        MOUSE, CAT = 1, 2
        S = N * N * 2
        status = bytearray(S)
        degree = [0] * S
        q = deque()
        for m in range(N):
            base = m * N
            for c in range(N):
                for t in range(2):
                    st = (base + c) * 2 + t
                    if m == fi:
                        status[st] = MOUSE
                        q.append(st)
                    elif c == fi or c == m:
                        status[st] = CAT
                        q.append(st)
                    else:
                        degree[st] = len(mouse_moves[m]) if t == 0 else len(cat_moves[c])
        while q:
            st = q.popleft()
            w = status[st]
            t = st & 1
            m, c = divmod(st >> 1, N)
            if t == 1:
                for mp in mouse_prev[m]:
                    p = ((mp * N) + c) * 2
                    if status[p]:
                        continue
                    if w == MOUSE:
                        status[p] = MOUSE
                        q.append(p)
                    else:
                        degree[p] -= 1
                        if degree[p] == 0:
                            status[p] = CAT
                            q.append(p)
            else:
                for cp in cat_prev[c]:
                    p = ((m * N) + cp) * 2 + 1
                    if status[p]:
                        continue
                    if w == CAT:
                        status[p] = CAT
                        q.append(p)
                    else:
                        degree[p] -= 1
                        if degree[p] == 0:
                            status[p] = MOUSE
                            q.append(p)
        return status[(mi * N + ci) * 2] == MOUSE
