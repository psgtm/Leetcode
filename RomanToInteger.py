class Solution:
    def romanToInt(self, s: str) -> int:
        # Define a dictionary mapping Roman numerals to their integer values
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Traverse the string in reverse order
        for char in reversed(s):
            # Get the integer value of the current Roman numeral
            curr_value = roman_to_int[char]
            
            # If the current value is less than the previous value, subtract it
            if curr_value < prev_value:
                total -= curr_value
            else:
                # Otherwise, add it to the total
                total += curr_value
            
            # Update previous value
            prev_value = curr_value
        
        return total
