"""
306. Additive Number
Difficulty: Medium
https://leetcode.com/problems/additive-number/

──────────────────────────────────────────────────

An additive number is a string whose digits can form an additive
sequence.

A valid additive sequence should contain at least three numbers.
Except for the first two numbers, each subsequent number in the
sequence must be the sum of the preceding two.

Given a string containing only digits, return true if it is an
additive number or false otherwise.

Note: Numbers in the additive sequence cannot have leading zeros, so
sequence 1, 2, 03 or 1, 02, 3 is invalid.

 

Example 1:

Input: "112358"
Output: true
Explanation: 
The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

Example 2:

Input: "199100199"
Output: true
Explanation: 
The additive sequence is: 1, 99, 100, 199. 
1 + 99 = 100, 99 + 100 = 199

 

Constraints:

	• 1 <= num.length <= 35

	• num consists only of digits.

 

Follow up: How would you handle overflow for very large input
integers?
"""

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def valid(a: str, b: str, start: int) -> bool:
            if (len(a) > 1 and a[0] == "0") or (len(b) > 1 and b[0] == "0"):
                return False
            while start < n:
                total = str(int(a) + int(b))
                if not num.startswith(total, start):
                    return False
                start += len(total)
                a, b = b, total
            return True

        for i in range(1, n):
            for j in range(i + 1, n):
                if valid(num[:i], num[i:j], j):
                    return True
        return False
