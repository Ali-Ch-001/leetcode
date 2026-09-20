class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand(left: int, right: int) -> str:
            # Expand outwards as long as characters match and indices are valid
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the valid palindrome substring
            # Note: left is decremented one step too far, right incremented one step too far
            # so we slice from left + 1 up to right
            return s[left + 1 : right]

        longest_str = ""

        for i in range(len(s)):
            # Case 1: Odd length palindrome (centered at i)
            # e.g., "aba" centered at 'b'
            odd_palindrome = expand(i, i)
            if len(odd_palindrome) > len(longest_str):
                longest_str = odd_palindrome
            
            # Case 2: Even length palindrome (centered between i and i+1)
            # e.g., "abba" centered between 'b' and 'b'
            even_palindrome = expand(i, i + 1)
            if len(even_palindrome) > len(longest_str):
                longest_str = even_palindrome
        
        return longest_str