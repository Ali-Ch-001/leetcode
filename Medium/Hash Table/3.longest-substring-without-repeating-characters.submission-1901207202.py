class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Stores character and its last seen index
        left = 0       # Start of the window
        max_length = 0

        for right, char in enumerate(s):
            # If we found a duplicate AND it's inside our current window
            if char in char_map and char_map[char] >= left:
                # Move the left pointer to the right of the duplicate
                left = char_map[char] + 1

            # Store/Update the character's index
            char_map[char] = right
            
            # Calculate max length (Window size = right - left + 1)
            max_length = max(max_length, right - left + 1)

        return max_length