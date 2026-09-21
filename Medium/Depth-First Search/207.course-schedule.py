"""
207. Course Schedule
Difficulty: Medium
https://leetcode.com/problems/course-schedule/

──────────────────────────────────────────────────

There are a total of numCourses courses you have to take, labeled
from 0 to numCourses - 1. You are given an array prerequisites where
prerequisites[i] = [ai, bi] indicates that you must take course bi
first if you want to take course ai.

• For example, the pair [0, 1], indicates that to take course 0 you
have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take
course 0 you should also have finished course 1. So it is impossible.

 

Constraints:

	• 1 <= numCourses <= 2000

	• 0 <= prerequisites.length <= 5000

	• prerequisites[i].length == 2

	• 0 <= ai, bi < numCourses

	• All the pairs prerequisites[i] are unique.
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        queue = [c for c in range(numCourses) if indegree[c] == 0]
        taken = 0
        while queue:
            course = queue.pop()
            taken += 1
            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        return taken == numCourses
