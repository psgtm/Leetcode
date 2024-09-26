class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        max_length = 0
        i = 0
        
        for j in range(len(s)):
            if s[j] in char_index_map and char_index_map[s[j]] >= i:
                i = char_index_map[s[j]] + 1
            char_index_map[s[j]] = j
            max_length = max(max_length, j - i + 1)
        
        return max_length
