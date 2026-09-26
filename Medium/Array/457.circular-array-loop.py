"""
457. Circular Array Loop
Difficulty: Medium
https://leetcode.com/problems/circular-array-loop/

──────────────────────────────────────────────────

You are playing a game involving a circular array of non-zero
integers nums. Each nums[i] denotes the number of indices
forward/backward you must move if you are located at index i:

	• If nums[i] is positive, move nums[i] steps forward, and

	• If nums[i] is negative, move abs(nums[i]) steps backward.

Since the array is circular, you may assume that moving forward from
the last element puts you on the first element, and moving backwards
from the first element puts you on the last element.

A cycle in the array consists of a sequence of indices seq of length
k where:

• Following the movement rules above results in the repeating index
sequence seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...

	• Every nums[seq[j]] is either all positive or all negative.

	• k > 1

Return true if there is a cycle in nums, or false otherwise.

 

Example 1:

Input: nums = [2,-1,1,2,2]
Output: true
Explanation: The graph shows how the indices are connected. White
nodes are jumping forward, while red is jumping backward.
We can see the cycle 0 --> 2 --> 3 --> 0 --> ..., and all of its
nodes are white (jumping in the same direction).

Example 2:

Input: nums = [-1,-2,-3,-4,-5,6]
Output: false
Explanation: The graph shows how the indices are connected. White
nodes are jumping forward, while red is jumping backward.
The only cycle is of size 1, so we return false.

Example 3:

Input: nums = [1,-1,5,1,4]
Output: true
Explanation: The graph shows how the indices are connected. White
nodes are jumping forward, while red is jumping backward.
We can see the cycle 0 --> 1 --> 0 --> ..., and while it is of size >
1, it has a node jumping forward and a node jumping backward, so it is
not a cycle.
We can see the cycle 3 --> 4 --> 3 --> ..., and all of its nodes are
white (jumping in the same direction).

 

Constraints:

	• 1 <= nums.length <= 5000

	• -1000 <= nums[i] <= 1000

	• nums[i] != 0

 

Follow up: Could you solve it in O(n) time complexity and O(1) extra
space complexity?
"""

class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                continue
            forward = nums[i] > 0
            slow = fast = i
            while True:
                slow = self._next(nums, slow, forward, n)
                fast = self._next(nums, fast, forward, n)
                if fast != -1:
                    fast = self._next(nums, fast, forward, n)
                if slow == -1 or fast == -1:
                    break
                if slow == fast:
                    return True
            j = i
            while nums[j] != 0 and (nums[j] > 0) == forward:
                nxt = (j + nums[j]) % n
                nums[j] = 0
                if nxt == j:
                    break
                j = nxt
        return False

    def _next(self, nums: list[int], index: int, forward: bool, n: int) -> int:
        if (nums[index] > 0) != forward:
            return -1
        nxt = (index + nums[index]) % n
        if nxt == index:
            return -1
        return nxt
