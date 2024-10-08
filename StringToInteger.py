class Solution:
    def myAtoi(self, s: str) -> int:
        i, n, sign, result = 0, len(s), 1, 0
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        
        while i < n and s[i] == ' ':
            i += 1
        
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        while i < n and s[i].isdigit():
            digit = int(s[i])
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            i += 1
        
        return sign * result
