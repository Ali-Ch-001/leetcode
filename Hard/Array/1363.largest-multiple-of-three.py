"""
1363. Largest Multiple of Three
Difficulty: Hard
https://leetcode.com/problems/largest-multiple-of-three/

──────────────────────────────────────────────────

Given an array of digits digits, return the largest multiple of three
that can be formed by concatenating some of the given digits in any
order. If there is no answer return an empty string.

Since the answer may not fit in an integer data type, return the
answer as a string. Note that the returning answer must not contain
unnecessary leading zeros.

 

Example 1:

Input: digits = [8,1,9]
Output: "981"

Example 2:

Input: digits = [8,6,7,1,0]
Output: "8760"

Example 3:

Input: digits = [1]
Output: ""

 

Constraints:

	• 1 <= digits.length <= 10^4

	• 0 <= digits[i] <= 9
"""

class Solution:
    def largestMultipleOfThree(self, digits: list[int]) -> str:
        cnt = [0] * 10
        for d in digits:
            cnt[d] += 1
        total = sum(digits)

        def remove_one(r):
            for d in range(r, 10, 3):
                if cnt[d]:
                    cnt[d] -= 1
                    return True
            return False

        if total % 3 == 1:
            if not remove_one(1):
                remove_one(2)
                remove_one(2)
        elif total % 3 == 2:
            if not remove_one(2):
                remove_one(1)
                remove_one(1)

        s = ''.join(str(d) * cnt[d] for d in range(9, -1, -1))
        s = s.lstrip('0')
        if not s:
            return '0' if any(cnt) else ''
        return s
        
