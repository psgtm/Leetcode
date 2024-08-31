from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the end of the list
        for i in range(len(digits) - 1, -1, -1):
            # If the current digit is less than 9, just add one to this digit
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, set it to 0 and move to the next digit
            digits[i] = 0
        
        # If all digits were 9, we need to add a 1 at the beginning
        return [1] + digits