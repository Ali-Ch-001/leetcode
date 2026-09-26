"""
546. Remove Boxes
Difficulty: Hard
https://leetcode.com/problems/remove-boxes/

──────────────────────────────────────────────────

You are given several boxes with different colors represented by
different positive numbers.

You may experience several rounds to remove boxes until there is no
box left. Each time you can choose some continuous boxes with the same
color (i.e., composed of k boxes, k >= 1), remove them and get k * k
points.

Return the maximum points you can get.

 

Example 1:

Input: boxes = [1,3,2,2,2,3,4,3,1]
Output: 23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
----> [1, 3, 3, 3, 1] (1*1=1 points) 
----> [1, 1] (3*3=9 points) 
----> [] (2*2=4 points)

Example 2:

Input: boxes = [1,1,1]
Output: 9

Example 3:

Input: boxes = [1]
Output: 1

 

Constraints:

	• 1 <= boxes.length <= 100

	• 1 <= boxes[i] <= 100
"""

class Solution:
    def removeBoxes(self, boxes: list[int]) -> int:
        memo = {}

        def dp(left: int, right: int, streak: int) -> int:
            if left > right:
                return 0
            if (left, right, streak) in memo:
                return memo[(left, right, streak)]
            while left < right and boxes[right] == boxes[right - 1]:
                right -= 1
                streak += 1
            best = (streak + 1) ** 2 + dp(left, right - 1, 0)
            for i in range(left, right):
                if boxes[i] == boxes[right]:
                    best = max(best, dp(left, i, streak + 1) + dp(i + 1, right - 1, 0))
            memo[(left, right, streak)] = best
            return best

        return dp(0, len(boxes) - 1, 0)
