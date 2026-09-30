"""
1345. Jump Game IV
Difficulty: Hard
https://leetcode.com/problems/jump-game-iv/

──────────────────────────────────────────────────

Given an array of integers arr, you are initially positioned at the
first index of the array.

In one step you can jump from index i to index:

	• i + 1 where: i + 1 < arr.length.

	• i - 1 where: i - 1 >= 0.

	• j where: arr[i] == arr[j] and i != j.

Return the minimum number of steps to reach the last index of the
array.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9.
Note that index 9 is the last index of the array.

Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You do not need to jump.

Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is
last index of the array.

 

Constraints:

	• 1 <= arr.length <= 5 * 10^4

	• -10^8 <= arr[i] <= 10^8
"""

from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        pos = defaultdict(list)
        for i, v in enumerate(arr):
            pos[v].append(i)
        visited = [False] * n
        visited[0] = True
        q = deque([0])
        steps = 0
        while q:
            steps += 1
            for _ in range(len(q)):
                i = q.popleft()
                for j in (i - 1, i + 1):
                    if 0 <= j < n and not visited[j]:
                        if j == n - 1:
                            return steps
                        visited[j] = True
                        q.append(j)
                for j in pos[arr[i]]:
                    if not visited[j]:
                        if j == n - 1:
                            return steps
                        visited[j] = True
                        q.append(j)
                del pos[arr[i]]
        return steps
