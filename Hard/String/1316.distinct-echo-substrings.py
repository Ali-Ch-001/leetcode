"""
1316. Distinct Echo Substrings
Difficulty: Hard
https://leetcode.com/problems/distinct-echo-substrings/

──────────────────────────────────────────────────

Return the number of distinct non-empty substrings of text that can
be written as the concatenation of some string with itself (i.e. it
can be written as a + a where a is some string).

 

Example 1:

Input: text = "abcabcabc"
Output: 3
Explanation: The 3 substrings are "abcabc", "bcabca" and "cabcab".

Example 2:

Input: text = "leetcodeleetcode"
Output: 2
Explanation: The 2 substrings are "ee" and "leetcodeleetcode".

 

Constraints:

	• 1 <= text.length <= 2000

	• text has only lowercase English letters.
"""

class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        mod = (1 << 61) - 1
        base = 131
        power = [1] * (n + 1)
        prefix = [0] * (n + 1)
        for i, ch in enumerate(text):
            power[i + 1] = power[i] * base % mod
            prefix[i + 1] = (prefix[i] * base + ord(ch)) % mod

        def get(lo, hi):
            return (prefix[hi] - prefix[lo] * power[hi - lo]) % mod

        seen = set()
        for half in range(1, n // 2 + 1):
            for i in range(n - 2 * half + 1):
                if get(i, i + half) == get(i + half, i + 2 * half):
                    seen.add(get(i, i + 2 * half))
        return len(seen)
        
