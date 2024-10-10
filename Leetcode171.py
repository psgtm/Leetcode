class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i, char in enumerate(reversed(columnTitle)):
            # ord('A') is 65, so we subtract 64 to make 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26
            result += (ord(char) - ord('A') + 1) * (26 ** i)
        return result