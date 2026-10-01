"""
1390. Four Divisors
Difficulty: Medium
https://leetcode.com/problems/four-divisors/

──────────────────────────────────────────────────

Given an integer array nums, return the sum of divisors of the
integers in that array that have exactly four divisors. If there is no
such integer in the array, return 0.

 

Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation: 
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.

Example 2:

Input: nums = [21,21]
Output: 64

Example 3:

Input: nums = [1,2,3,4,5]
Output: 0

 

Constraints:

	• 1 <= nums.length <= 10^4

	• 1 <= nums[i] <= 10^5
"""

class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        total = 0
        for x in nums:
            divs = []
            i = 1
            while i * i <= x:
                if x % i == 0:
                    divs.append(i)
                    if i != x // i:
                        divs.append(x // i)
                    if len(divs) > 4:
                        break
                i += 1
            if len(divs) == 4:
                total += sum(divs)
        return total
        
