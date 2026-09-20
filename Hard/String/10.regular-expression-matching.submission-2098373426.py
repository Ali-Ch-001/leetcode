class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        
        def dp(i: int, j: int) -> bool:
            # Return cached result if we've already computed this state
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base Case: If we've reached the end of the pattern, 
            # the string must also be at the end to be a valid match.
            if j == len(p):
                return i == len(s)
            
            # Check if the current characters match
            first_match = i < len(s) and p[j] in {s[i], '.'}
            
            # If the next character in the pattern is a '*'
            if j + 1 < len(p) and p[j+1] == '*':
                # We have two choices:
                # 1. Zero occurrences: Skip the current pattern character and the '*' (move j by 2)
                # 2. One or more occurrences: If the first characters match, consume one character 
                #    from the string (move i by 1) and keep the pattern exactly where it is.
                ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # Standard character matching: advance both pointers
                ans = first_match and dp(i + 1, j + 1)
                
            memo[(i, j)] = ans
            return ans
        
        return dp(0, 0)