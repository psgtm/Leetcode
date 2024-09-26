from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string as the potential prefix
        prefix = strs[0]
        
        # Iterate through all the strings in the list
        for string in strs[1:]:
            # Reduce the prefix until it matches the start of the string
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
