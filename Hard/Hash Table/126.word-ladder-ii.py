"""
126. Word Ladder II
Difficulty: Hard
https://leetcode.com/problems/word-ladder-ii/

──────────────────────────────────────────────────

A transformation sequence from word beginWord to word endWord using a
dictionary wordList is a sequence of words beginWord -> s1 -> s2 ->
... -> sk such that:

	• Every adjacent pair of words differs by a single letter.

• Every si for 1 <= i <= k is in wordList. Note that beginWord does
not need to be in wordList.

	• sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList,
return all the shortest transformation sequences from beginWord to
endWord, or an empty list if no such sequence exists. Each sequence
should be returned as a list of the words [beginWord, s1, s2, ...,
sk].

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList =
["hot","dot","dog","lot","log","cog"]
Output:
[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"

Example 2:

Input: beginWord = "hit", endWord = "cog", wordList =
["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is
no valid transformation sequence.

 

Constraints:

	• 1 <= beginWord.length <= 5

	• endWord.length == beginWord.length

	• 1 <= wordList.length <= 500

	• wordList[i].length == beginWord.length

• beginWord, endWord, and wordList[i] consist of lowercase English
letters.

	• beginWord != endWord

	• All the words in wordList are unique.

• The sum of all shortest transformation sequences does not exceed
10^5.
"""

from collections import deque, defaultdict


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        words = set(wordList)
        if endWord not in words:
            return []
        parents = defaultdict(list)
        distance = {beginWord: 0}
        queue = deque([beginWord])
        while queue:
            word = queue.popleft()
            if word == endWord:
                break
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    nxt = word[:i] + ch + word[i + 1:]
                    if nxt in words:
                        if nxt not in distance:
                            distance[nxt] = distance[word] + 1
                            parents[nxt] = [word]
                            queue.append(nxt)
                        elif distance[nxt] == distance[word] + 1:
                            parents[nxt].append(word)
        if endWord not in distance:
            return []
        results = []
        path = [endWord]

        def backtrack(word: str) -> None:
            if word == beginWord:
                results.append(path[::-1])
                return
            for parent in parents[word]:
                path.append(parent)
                backtrack(parent)
                path.pop()

        backtrack(endWord)
        return results
