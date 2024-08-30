class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Check if the needle is an empty string
        if not needle:
            return 0
        
        # Get the length of the needle
        len_needle = len(needle)
        
        # Iterate through the haystack
        for i in range(len(haystack) - len_needle + 1):
            # Check if the substring matches the needle
            if haystack[i:i+len_needle] == needle:
                return i
        
        # Return -1 if the needle is not found
        return -1
