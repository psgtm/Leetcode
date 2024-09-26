class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Convert the number to a string to check if it reads the same forwards and backwards
        x_str = str(x)
        return x_str == x_str[::-1]
