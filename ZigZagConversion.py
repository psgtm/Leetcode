class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case where numRows is 1, return the original string
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize a list of strings to store characters for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Iterate over each character in the string
        for char in s:
            rows[current_row] += char  # Append the character to the current row
            
            # Determine if we need to go down or up in the zigzag pattern
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move to the next row based on the current direction
            current_row += 1 if going_down else -1
        
        # Combine all rows to form the final zigzag string
        return ''.join(rows)
