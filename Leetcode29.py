class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Define INT_MAX and INT_MIN for 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle edge case where result would overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with positive values
        dividend, divisor = abs(dividend), abs(divisor)
        
        # Initialize the quotient
        quotient = 0
        
        # Use bit manipulation to speed up the division
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            # Subtract the largest shifted divisor from the dividend
            dividend -= temp_divisor
            # Add the corresponding multiple to the quotient
            quotient += multiple
        
        # Apply the sign to the result
        if negative:
            quotient = -quotient
        
        # Ensure the result is within the 32-bit integer range
        return min(max(quotient, INT_MIN), INT_MAX)
