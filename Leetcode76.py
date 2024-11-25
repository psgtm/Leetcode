from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # Count characters in t
        target_count = Counter(t)
        required = len(target_count)  # Number of unique characters in t
        left, right = 0, 0  # Sliding window pointers
        formed = 0  # Number of characters in the current window that meet target_count
        window_count = {}
        
        # Result: (window length, left, right)
        result = float("inf"), None, None
        
        while right < len(s):
            # Add the character at the right pointer to the window
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            # Check if this character's count matches the target count
            if char in target_count and window_count[char] == target_count[char]:
                formed += 1
            
            # Try and contract the window until it ceases to be valid
            while left <= right and formed == required:
                char = s[left]
                
                # Save the smallest window
                if right - left + 1 < result[0]:
                    result = (right - left + 1, left, right)
                
                # Remove the leftmost character from the window
                window_count[char] -= 1
                if char in target_count and window_count[char] < target_count[char]:
                    formed -= 1
                
                left += 1  # Move the left pointer forward
            
            # Expand the window
            right += 1
        
        # Return the smallest window or an empty string if no window was found
        return "" if result[0] == float("inf") else s[result[1]:result[2] + 1]
