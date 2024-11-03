from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals by their start times
        intervals.sort(key=lambda x: x[0])
        
        # Initialize the list to hold merged intervals
        merged = []
        
        for interval in intervals:
            # If merged is empty or if the current interval does not overlap with the last merged interval
            if not merged or merged[-1][1] < interval[0]:
                # Add the current interval to merged
                merged.append(interval)
            else:
                # There is overlap, so merge the current interval with the previous one
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
