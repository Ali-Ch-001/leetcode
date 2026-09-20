class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If there's only 1 row or the string is shorter than the number of rows,
        # the zigzag pattern doesn't change the string.
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize an array of strings to represent each row
        rows = [''] * numRows
        
        current_row = 0
        going_down = False
        
        # Traverse the string and place characters in appropriate rows
        for char in s:
            rows[current_row] += char
            
            # Change direction if we hit the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
                
            # Move to the next row
            current_row += 1 if going_down else -1
            
        # Concatenate all rows to get the final string
        return "".join(rows)