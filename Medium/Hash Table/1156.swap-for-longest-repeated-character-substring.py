"""
1156. Swap For Longest Repeated Character Substring
Difficulty: Medium
https://leetcode.com/problems/swap-for-longest-repeated-character-substring/

──────────────────────────────────────────────────

You are given a string text. You can swap two of the characters in
the text.

Return the length of the longest substring with repeated characters.

 

Example 1:

Input: text = "ababa"
Output: 3
Explanation: We can swap the first 'b' with the last 'a', or the last
'b' with the first 'a'. Then, the longest repeated character substring
is "aaa" with length 3.

Example 2:

Input: text = "aaabaaa"
Output: 6
Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we
get longest repeated character substring "aaaaaa" with length 6.

Example 3:

Input: text = "aaaaa"
Output: 5
Explanation: No need to swap, longest repeated character substring is
"aaaaa" with length is 5.

 

Constraints:

	• 1 <= text.length <= 2 * 10^4

	• text consist of lowercase English characters only.
"""

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        from collections import Counter
        freq = Counter(text)
        runs = []
        for ch in text:
            if runs and runs[-1][0] == ch:
                runs[-1][1] += 1
            else:
                runs.append([ch, 1])
        ans = 0
        for ch, length in runs:
            ans = max(ans, min(freq[ch], length + 1))
        for i in range(1, len(runs) - 1):
            if runs[i - 1][0] == runs[i + 1][0] and runs[i][1] == 1:
                ch = runs[i - 1][0]
                combined = runs[i - 1][1] + runs[i + 1][1]
                ans = max(ans, combined + (1 if freq[ch] > combined else 0))
        return ans

