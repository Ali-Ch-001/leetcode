from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate the area with the current left and right pointers
            current_area = min(height[left], height[right]) * (right - left)
            
            # Update the maximum area found so far
            if current_area > max_area:
                max_area = current_area
            
            # Move the pointer that points to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area