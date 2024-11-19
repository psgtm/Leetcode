# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # This will eventually become the new head
        current = head
        
        while current:  # Traverse the list
            next_node = current.next  # Save the next node
            current.next = prev  # Reverse the current node's pointer
            prev = current  # Move prev forward
            current = next_node  # Move current forward
        
        return prev  # New head of the reversed list
