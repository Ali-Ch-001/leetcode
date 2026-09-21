"""
420. Strong Password Checker
Difficulty: Hard
https://leetcode.com/problems/strong-password-checker/

──────────────────────────────────────────────────

A password is considered strong if the below conditions are all met:

	• It has at least 6 characters and at most 20 characters.

• It contains at least one lowercase letter, at least one uppercase
letter, and at least one digit.

• It does not contain three repeating characters in a row (i.e.,
"Baaabb0" is weak, but "Baaba0" is strong).

Given a string password, return the minimum number of steps required
to make password strong. if password is already strong, return 0.

In one step, you can:

	• Insert one character to password,

	• Delete one character from password, or

	• Replace one character of password with another character.

 

Example 1:

Input: password = "a"
Output: 5

Example 2:

Input: password = "aA1"
Output: 3

Example 3:

Input: password = "1337C0d3"
Output: 0

 

Constraints:

	• 1 <= password.length <= 50

• password consists of letters, digits, dot '.' or exclamation mark
'!'.
"""

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        missing = 0
        if not any(ch.islower() for ch in password):
            missing += 1
        if not any(ch.isupper() for ch in password):
            missing += 1
        if not any(ch.isdigit() for ch in password):
            missing += 1
        change = 0
        one = two = 0
        i = 0
        while i < n:
            length = 1
            while i + length < n and password[i + length] == password[i]:
                length += 1
            if length >= 3:
                change += length // 3
                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1
            i += length
        if n < 6:
            return max(missing, 6 - n)
        if n <= 20:
            return max(missing, change)
        delete = n - 20
        change -= min(delete, one)
        change -= min(max(delete - one, 0), two * 2) // 2
        change -= max(delete - one - 2 * two, 0) // 3
        return delete + max(missing, change)
