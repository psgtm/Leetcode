from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge nums2 into nums1 as one sorted array in-place.
        """
        # Start filling from the last position
        i, j, k = m - 1, n - 1, m + n - 1
        
        # While both arrays have elements
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If there are remaining elements in nums2, place them in nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
