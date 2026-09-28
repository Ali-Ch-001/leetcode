"""
818. Race Car
Difficulty: Hard
https://leetcode.com/problems/race-car/

──────────────────────────────────────────────────

Your car starts at position 0 and speed +1 on an infinite number
line. Your car can go into negative positions. Your car drives
automatically according to a sequence of instructions 'A' (accelerate)
and 'R' (reverse):

	• When you get an instruction 'A', your car does the following:

	
		• position += speed

		• speed *= 2

	
	

	• When you get an instruction 'R', your car does the following:
	
		• If your speed is positive then speed = -1

		• otherwise speed = 1

	
	Your position stays the same.

For example, after commands "AAR", your car goes to positions 0 --> 1
--> 3 --> 3, and your speed goes to 1 --> 2 --> 4 --> -1.

Given a target position target, return the length of the shortest
sequence of instructions to get there.

 

Example 1:

Input: target = 3
Output: 2
Explanation: 
The shortest instruction sequence is "AA".
Your position goes from 0 --> 1 --> 3.

Example 2:

Input: target = 6
Output: 5
Explanation: 
The shortest instruction sequence is "AAARA".
Your position goes from 0 --> 1 --> 3 --> 7 --> 7 --> 6.

 

Constraints:

	• 1 <= target <= 10^4
"""

from functools import lru_cache


class Solution:
    def racecar(self, target: int) -> int:
        @lru_cache(maxsize=None)
        def dp(t):
            if t == 0:
                return 0
            k = t.bit_length()
            if t == (1 << k) - 1:
                return k
            best = dp((1 << k) - 1 - t) + k + 1
            for i in range(k - 1):
                best = min(best, dp(t - (1 << (k - 1)) + (1 << i)) + k + i + 1)
            return best

        return dp(target)
