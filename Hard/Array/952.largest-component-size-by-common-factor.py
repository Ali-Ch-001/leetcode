"""
952. Largest Component Size by Common Factor
Difficulty: Hard
https://leetcode.com/problems/largest-component-size-by-common-factor/

──────────────────────────────────────────────────

You are given an integer array of unique positive integers nums.
Consider the following graph:

• There are nums.length nodes, labeled nums[0] to nums[nums.length -
1],

• There is an undirected edge between nums[i] and nums[j] if nums[i]
and nums[j] share a common factor greater than 1.

Return the size of the largest connected component in the graph.

 

Example 1:

Input: nums = [4,6,15,35]
Output: 4

Example 2:

Input: nums = [20,50,9,63]
Output: 2

Example 3:

Input: nums = [2,3,6,7,4,12,21,39]
Output: 8

 

Constraints:

	• 1 <= nums.length <= 2 * 10^4

	• 1 <= nums[i] <= 10^5

	• All the values of nums are unique.
"""

class Solution:
    def largestComponentSize(self, nums: list[int]) -> int:
        limit = max(nums)
        parent = list(range(limit + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            parent[find(a)] = find(b)

        for value in nums:
            x = value
            divisor = 2
            while divisor * divisor <= x:
                if x % divisor == 0:
                    union(value, divisor)
                    while x % divisor == 0:
                        x //= divisor
                divisor += 1
            if x > 1:
                union(value, x)
        counts = {}
        best = 0
        for value in nums:
            root = find(value)
            counts[root] = counts.get(root, 0) + 1
            best = max(best, counts[root])
        return best
