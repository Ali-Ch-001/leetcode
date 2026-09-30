"""
1349. Maximum Students Taking Exam
Difficulty: Hard
https://leetcode.com/problems/maximum-students-taking-exam/

──────────────────────────────────────────────────

Given a m * n matrix seats  that represent seats distributions in a
classroom. If a seat is broken, it is denoted by '#' character
otherwise it is denoted by a '.' character.

Students can see the answers of those sitting next to the left,
right, upper left and upper right, but he cannot see the answers of
the student sitting directly in front or behind him. Return the
maximum number of students that can take the exam together without any
cheating being possible.

Students must be placed in seats in good condition.

 

Example 1:

Input: seats = [["#",".","#","#",".","#"],
                [".","#","#","#","#","."],
                ["#",".","#","#",".","#"]]
Output: 4
Explanation: Teacher can place 4 students in available seats so they
don't cheat on the exam.

Example 2:

Input: seats = [[".","#"],
                ["#","#"],
                ["#","."],
                ["#","#"],
                [".","#"]]
Output: 3
Explanation: Place all students in available seats. 

Example 3:

Input: seats = [["#",".",".",".","#"],
                [".","#",".","#","."],
                [".",".","#",".","."],
                [".","#",".","#","."],
                ["#",".",".",".","#"]]
Output: 10
Explanation: Place students in available seats in column 1, 3 and 5.

 

Constraints:

	• seats contains only characters '.' and'#'.

	• m == seats.length

	• n == seats[i].length

	• 1 <= m <= 8

	• 1 <= n <= 8
"""

class Solution:
    def maxStudents(self, seats: list[list[str]]) -> int:
        m, n = len(seats), len(seats[0])
        avail = []
        for row in seats:
            mask = 0
            for j, c in enumerate(row):
                if c == ".":
                    mask |= 1 << j
            avail.append(mask)
        valid = [
            mask
            for mask in range(1 << n)
            if not (mask & (mask << 1)) and not (mask & (mask >> 1))
        ]
        prev_dp = {0: 0}
        for i in range(m):
            cur_dp = {}
            for mask in valid:
                if mask & ~avail[i]:
                    continue
                best = -1
                for pmask, val in prev_dp.items():
                    if mask & (pmask << 1) or mask & (pmask >> 1):
                        continue
                    if val > best:
                        best = val
                if best >= 0:
                    cur_dp[mask] = best + bin(mask).count("1")
            prev_dp = cur_dp
        return max(prev_dp.values())
