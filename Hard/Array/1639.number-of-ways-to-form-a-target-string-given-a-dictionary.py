"""
1639. Number of Ways to Form a Target String Given a Dictionary
Difficulty: Hard
https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

──────────────────────────────────────────────────

You are given a list of strings of the same length words and a string
target.

Your task is to form target using the given words under the following
rules:

	• target should be formed from left to right.

• To form the i^th character (0-indexed) of target, you can choose
the k^th character of the j^th string in words if target[i] =
words[j][k].

• Once you use the k^th character of the j^th string of words, you
can no longer use the x^th character of any string in words where x <=
k. In other words, all characters to the left of or at index k become
unusuable for every string.

	• Repeat the process until you form the string target.

Notice that you can use multiple characters from the same string in
words provided the conditions above are met.

Return the number of ways to form target from words. Since the answer
may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: words = ["acca","bbbb","caca"], target = "aba"
Output: 6
Explanation: There are 6 ways to form target.
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")

Example 2:

Input: words = ["abba","baab"], target = "bab"
Output: 4
Explanation: There are 4 ways to form target.
"bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
"bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
"bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
"bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")

 

Constraints:

	• 1 <= words.length <= 1000

	• 1 <= words[i].length <= 1000

	• All strings in words have the same length.

	• 1 <= target.length <= 1000

	• words[i] and target contain only lowercase English letters.
"""

class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        MOD = 10**9 + 7
        width = len(words[0])
        cnt = [[0] * 26 for _ in range(width)]
        for w in words:
            for k, ch in enumerate(w):
                cnt[k][ord(ch) - 97] += 1
        T = len(target)
        t_idx = [ord(ch) - 97 for ch in target]
        dp = [0] * (T + 1)
        dp[0] = 1
        for k in range(width):
            c = cnt[k]
            upper = k + 1 if k + 1 < T else T
            for j in range(upper, 0, -1):
                ways = c[t_idx[j - 1]]
                if ways:
                    dp[j] = (dp[j] + dp[j - 1] * ways) % MOD
        return dp[T]
        
