"""
1125. Smallest Sufficient Team
Difficulty: Hard
https://leetcode.com/problems/smallest-sufficient-team/

──────────────────────────────────────────────────

In a project, you have a list of required skills req_skills, and a
list of people. The i^th person people[i] contains a list of skills
that the person has.

Consider a sufficient team: a set of people such that for every
required skill in req_skills, there is at least one person in the team
who has that skill. We can represent these teams by the index of each
person.

• For example, team = [0, 1, 3] represents the people with skills
people[0], people[1], and people[3].

Return any sufficient team of the smallest possible size, represented
by the index of each person. You may return the answer in any order.

It is guaranteed an answer exists.

 

Example 1:

Input: req_skills = ["java","nodejs","reactjs"], people =
[["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]

Example 2:

Input: req_skills =
["algorithms","math","java","reactjs","csharp","aws"], people =
[["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
Output: [1,2]

 

Constraints:

	• 1 <= req_skills.length <= 16

	• 1 <= req_skills[i].length <= 16

	• req_skills[i] consists of lowercase English letters.

	• All the strings of req_skills are unique.

	• 1 <= people.length <= 60

	• 0 <= people[i].length <= 16

	• 1 <= people[i][j].length <= 16

	• people[i][j] consists of lowercase English letters.

	• All the strings of people[i] are unique.

	• Every skill in people[i] is a skill in req_skills.

	• It is guaranteed a sufficient team exists.
"""

class Solution:
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:
        m = len(req_skills)
        full = (1 << m) - 1
        skill_index = {skill: i for i, skill in enumerate(req_skills)}

        people_masks = []
        for person in people:
            mask = 0
            for skill in person:
                mask |= 1 << skill_index[skill]
            people_masks.append(mask)

        inf = float("inf")
        dp = [inf] * (1 << m)
        parent = [(-1, -1)] * (1 << m)
        dp[0] = 0

        for i, mask in enumerate(people_masks):
            if mask == 0:
                continue
            for current in range(full + 1):
                if dp[current] == inf:
                    continue
                nxt = current | mask
                if dp[current] + 1 < dp[nxt]:
                    dp[nxt] = dp[current] + 1
                    parent[nxt] = (current, i)

        team = []
        current = full
        while current:
            previous, person = parent[current]
            team.append(person)
            current = previous
        return team
