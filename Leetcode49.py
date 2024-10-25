from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)  # Using a defaultdict to group anagrams together

        for word in strs:
            # Sort each word, then use it as a key in the dictionary
            sorted_word = ''.join(sorted(word))
            anagram_dict[sorted_word].append(word)
        
        # Return all groups of anagrams as a list of lists
        return list(anagram_dict.values())
