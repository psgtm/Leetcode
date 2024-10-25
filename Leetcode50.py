class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle the case where n is negative
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1  # Initialize result
        
        while n > 0:
            # If n is odd, multiply result by x
            if n % 2 == 1:
                result *= x
            
            # Square x and halve n
            x *= x
            n //= 2
        
        return result
