class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        # Iterative Cartesian product via list comprehension
        res = [""]
        for d in digits:
            res = [prefix + ch for prefix in res for ch in mapping[d]]

        return res