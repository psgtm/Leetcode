class Solution:
    def isNumber(self, s: str) -> bool:
        import re

        # Regular expression for a valid number
        pattern = r'^[+-]?((\d+(\.\d*)?)|(\.\d+))(e[+-]?\d+)?$'
        return re.match(pattern, s.strip()) is not None
