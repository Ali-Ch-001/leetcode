"""
345. Reverse Vowels of a String
Difficulty: Easy
https://leetcode.com/problems/reverse-vowels-of-a-string/

──────────────────────────────────────────────────

Given a string s, reverse only all the vowels in the string and
return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in
both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s
becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

	• 1 <= s.length <= 3 * 10^5

	• s consist of printable ASCII characters.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)
        left, right = 0, len(chars) - 1
        while left < right:
            while left < right and chars[left] not in vowels:
                left += 1
            while left < right and chars[right] not in vowels:
                right -= 1
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        return "".join(chars)
