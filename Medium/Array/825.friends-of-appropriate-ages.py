"""
825. Friends Of Appropriate Ages
Difficulty: Medium
https://leetcode.com/problems/friends-of-appropriate-ages/

──────────────────────────────────────────────────

There are n persons on a social media website. You are given an
integer array ages where ages[i] is the age of the i^th person.

A Person x will not send a friend request to a person y (x != y) if
any of the following conditions is true:

	• age[y] <= 0.5 * age[x] + 7

	• age[y] > age[x]

	• age[y] > 100 && age[x] < 100

Otherwise, x will send a friend request to y.

Note that if x sends a request to y, y will not necessarily send a
request to x. Also, a person will not send a friend request to
themself.

Return the total number of friend requests made.

 

Example 1:

Input: ages = [16,16]
Output: 2
Explanation: 2 people friend request each other.

Example 2:

Input: ages = [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.

Example 3:

Input: ages = [20,30,100,110,120]
Output: 3
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 ->
100.

 

Constraints:

	• n == ages.length

	• 1 <= n <= 2 * 10^4

	• 1 <= ages[i] <= 120
"""

class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        counts = {}
        for age in ages:
            counts[age] = counts.get(age, 0) + 1
        total = 0
        for age_a in counts:
            for age_b in counts:
                if age_b <= 0.5 * age_a + 7 or age_b > age_a:
                    continue
                total += counts[age_a] * counts[age_b]
                if age_a == age_b:
                    total -= counts[age_a]
        return total
