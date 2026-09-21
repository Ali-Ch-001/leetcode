"""
423. Reconstruct Original Digits from English
Difficulty: Medium
https://leetcode.com/problems/reconstruct-original-digits-from-english/

──────────────────────────────────────────────────

Given a string s containing an out-of-order English representation of
digits 0-9, return the digits in ascending order.

 

Example 1:

Input: s = "owoztneoer"
Output: "012"

Example 2:

Input: s = "fviefuro"
Output: "45"

 

Constraints:

	• 1 <= s.length <= 10^5

• s[i] is one of the characters
["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"].

	• s is guaranteed to be valid.
"""

class Solution:
    def originalDigits(self, s: str) -> str:
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

        def take(digit: int, word: str, letter: str) -> str:
            amount = counts.get(letter, 0)
            if amount:
                for ch in word:
                    counts[ch] -= amount
            return str(digit) * amount

        digits = []
        digits.append(take(0, "zero", "z"))
        digits.append(take(2, "two", "w"))
        digits.append(take(4, "four", "u"))
        digits.append(take(6, "six", "x"))
        digits.append(take(8, "eight", "g"))
        digits.append(take(1, "one", "o"))
        digits.append(take(3, "three", "t"))
        digits.append(take(5, "five", "f"))
        digits.append(take(7, "seven", "s"))
        digits.append(take(9, "nine", "i"))
        return "".join(sorted(digits))
