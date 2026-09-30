"""
1307. Verbal Arithmetic Puzzle
Difficulty: Hard
https://leetcode.com/problems/verbal-arithmetic-puzzle/

──────────────────────────────────────────────────

Given an equation, represented by words on the left side and the
result on the right side.

You need to check if the equation is solvable under the following
rules:

	• Each character is decoded as one digit (0 - 9).

	• No two characters can map to the same digit.

• Each words[i] and result are decoded as one number without leading
zeros.

• Sum of numbers on the left side (words) will equal to the number
on the right side (result).

Return true if the equation is solvable, otherwise return false.

 

Example 1:

Input: words = ["SEND","MORE"], result = "MONEY"
Output: true
Explanation: Map 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0,
'R'->8, 'Y'->'2'
Such that: "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652

Example 2:

Input: words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
Output: true
Explanation: Map 'S'-> 6, 'I'->5, 'X'->0, 'E'->8, 'V'->7, 'N'->2,
'T'->1, 'W'->'3', 'Y'->4
Such that: "SIX" + "SEVEN" + "SEVEN" = "TWENTY" ,  650 + 68782 +
68782 = 138214

Example 3:

Input: words = ["LEET","CODE"], result = "POINT"
Output: false
Explanation: There is no possible mapping to satisfy the equation, so
we return false.
Note that two different characters cannot map to the same digit.

 

Constraints:

	• 2 <= words.length <= 5

	• 1 <= words[i].length, result.length <= 7

	• words[i], result contain only uppercase English letters.

• The number of different characters used in the expression is at
most 10.
"""

class Solution:
    def isSolvable(self, words: list[str], result: str) -> bool:
        chars = set(''.join(words)) | set(result)
        if len(chars) > 10:
            return False

        rwords = [w[::-1] for w in words]
        rresult = result[::-1]
        max_len = max(len(w) for w in rwords + [rresult])
        lead = set(w[0] for w in words + [result] if len(w) > 1)

        assigned = {}
        used = [False] * 10

        def left_chars(col: int) -> list[str]:
            return [w[col] for w in rwords if col < len(w)]

        def dfs(col: int, idx: int, col_sum: int, carry: int) -> bool:
            if col == max_len:
                return carry == 0
            lchars = left_chars(col)
            if idx < len(lchars):
                ch = lchars[idx]
                if ch in assigned:
                    return dfs(col, idx + 1, col_sum + assigned[ch], carry)
                for d in range(10):
                    if used[d] or (d == 0 and ch in lead):
                        continue
                    assigned[ch] = d
                    used[d] = True
                    if dfs(col, idx + 1, col_sum + d, carry):
                        return True
                    del assigned[ch]
                    used[d] = False
                return False
            s = col_sum + carry
            digit = s % 10
            ncarry = s // 10
            rchar = rresult[col] if col < len(rresult) else None
            if rchar is None:
                if digit != 0:
                    return False
                return dfs(col + 1, 0, 0, ncarry)
            if rchar in assigned:
                if assigned[rchar] != digit:
                    return False
                return dfs(col + 1, 0, 0, ncarry)
            if used[digit] or (digit == 0 and rchar in lead):
                return False
            assigned[rchar] = digit
            used[digit] = True
            if dfs(col + 1, 0, 0, ncarry):
                return True
            del assigned[rchar]
            used[digit] = False
            return False

        return dfs(0, 0, 0, 0)
