"""
1871. Jump Game VII
Difficulty: Medium
https://leetcode.com/problems/jump-game-vii/

──────────────────────────────────────────────────

You are given a 0-indexed binary string s and two integers minJump
and maxJump. In the beginning, you are standing at index 0, which is
equal to '0'. You can move from index i to index j if the following
conditions are fulfilled:

	• i + minJump <= j <= min(i + maxJump, s.length - 1), and

	• s[j] == '0'.

Return true if you can reach index s.length - 1 in s, or false
otherwise.

 

Example 1:

Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.

Example 2:

Input: s = "01101110", minJump = 2, maxJump = 3
Output: false

 

Constraints:

	• 2 <= s.length <= 10^5

	• s[i] is either '0' or '1'.

	• s[0] == '0'

	• 1 <= minJump <= maxJump < s.length
"""

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        reach = [False] * n
        reach[0] = True
        pref = [0] * (n + 1)
        for i in range(1, n):
            if s[i] == '0':
                hi = i - minJump
                if hi >= 0:
                    lo = max(0, i - maxJump)
                    reach[i] = pref[hi + 1] - pref[lo] > 0
            pref[i + 1] = pref[i] + (1 if reach[i] else 0)
        return reach[n - 1]

