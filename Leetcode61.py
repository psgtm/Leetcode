# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Determine the length of the list
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        
        # Step 2: Connect the last node to the head to make it circular
        current.next = head
        
        # Step 3: Find the new head and new tail
        k = k % length  # Effective rotation
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
        
        # Step 4: Set the new head and break the cycle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
