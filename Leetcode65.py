class Solution:
    def isNumber(self, s: str) -> bool:
        def isInteger(s):
            if not s:
                return False
            if s[0] in ['+', '-']:
                s = s[1:]
            return s.isdigit()

        def isDecimal(s):
            if not s:
                return False
            if s[0] in ['+', '-']:
                s = s[1:]
            if '.' not in s:
                return False
            integer_part, dot, decimal_part = s.partition('.')
            if not integer_part and not decimal_part:
                return False
            if integer_part and not integer_part.isdigit():
                return False
            if decimal_part and not decimal_part.isdigit():
                return False
            return True

        s = s.strip()
        if 'e' in s or 'E' in s:
            base, _, exponent = s.partition('e') if 'e' in s else s.partition('E')
            return (isInteger(base) or isDecimal(base)) and isInteger(exponent)
        return isInteger(s) or isDecimal(s)
