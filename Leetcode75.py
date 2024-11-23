from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointers for the three regions
        low, mid, high = 0, 0, len(nums) - 1
        
        # Traverse the array
        while mid <= high:
            if nums[mid] == 0:
                # Swap the 0 to the 'low' region
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # Leave the 1 in the middle region
                mid += 1
            else:
                # Swap the 2 to the 'high' region
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
