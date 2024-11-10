from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        # Initialize variables
        word_len = len(words[0])
        word_count = len(words)
        concat_len = word_len * word_count
        word_map = Counter(words)  # Count of each word in words
        
        result = []
        
        # Slide over each possible starting point within the word length
        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()
            while right + word_len <= len(s):
                # Get the word from the current position
                word = s[right:right + word_len]
                right += word_len
                
                # If the word is in the map, add to current window count
                if word in word_map:
                    current_count[word] += 1
                    
                    # If more occurrences than required, move left pointer
                    while current_count[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        left += word_len
                    
                    # Check if we have a valid window
                    if right - left == concat_len:
                        result.append(left)
                
                # If word is not in the map, reset the window
                else:
                    current_count.clear()
                    left = right
        
        return result
