class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # The common prefix of the whole array is simply the common prefix
        # between the lexicographically smallest and largest strings.
        s1 = min(strs)
        s2 = max(strs)

        for i, ch in enumerate(s1):
            if ch != s2[i]:
                return s1[:i]

        return s1